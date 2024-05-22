from flask import Flask, render_template, request, jsonify
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import random
import pyjokes

app = Flask(__name__)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def how_are_you_response():
    responses = [
        "I'm doing well, thank you.",
        "I'm fine, thanks.",
        "I'm alright, thanks for asking.",
        "I'm doing okay, just taking things one step at a time.",
        "I'm doing fine, nothing out of the ordinary."
    ]
    return random.choice(responses)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_command():
    data = request.get_json()
    command = data.get('command', '')

    if 'hey lex' in command or 'hi lex' in command:
        response = 'How can I help you today?'
        talk(response)

    elif 'thank you' in command or 'stop' in command:
        response = "Goodbye!"
        talk(response)

    elif 'play' in command and ('song' in command or 'me a song' in command):
        response = "Yes, can you tell me the name and artist?"
        talk(response)
        song_command = "shape of you by ed sheeran"  # Example
        parts = song_command.split(' by ')
        song = parts[0].strip()
        artist = parts[1].strip() if len(parts) > 1 else None
        search_query = f"{song} {artist}" if artist else song
        if artist:
            response = "Playing " + song + ' by ' + artist
        else:
            response = "Playing " + song
        pywhatkit.playonyt(search_query)

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        response = 'Current time is ' + current_time
        talk(response)

    elif 'question' in command:
        question = command.replace('question', '').strip()
        info = wikipedia.summary(question, sentences=1)
        response = info
        talk(response)

    elif 'how are you' in command:
        response = how_are_you_response()
        talk(response)

    elif 'joke' in command:
        response = pyjokes.get_joke()
        talk(response)

    else:
        response = 'I didn’t get you'
        talk(response)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
