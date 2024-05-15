import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import random
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def how_are_you_response():
    responses = [
        "I'm doing well, thank you. How about yourself?",
        "I'm fine, thanks. How are you?",
        "I'm alright, thanks for asking.",
        "I'm doing okay, just taking things one step at a time.",
        "I'm doing fine, nothing out of the ordinary. How about you?"
    ]
    return random.choice(responses)

def take_command():
    command = ""  
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()             
    except Exception as e:
        print(e)
    return command

def run_nova():
    while True:
        command = take_command()
        if 'hey nova' in command or 'hi nova' in command:
            talk('How can I help you today?')

        elif 'stop it nova' in command:
            talk("Goodbye!")
            break

        elif 'play' in command and ('song' in command or 'me a song' in command):
            talk("Yes, can you tell me the name and artist?")
            song_command = take_command()
            parts = song_command.split(' by ')
            song = parts[0].strip()
            artist = parts[1].strip() if len(parts) > 1 else None
            search_query = f"{song} {artist}" if artist else song
            if artist:
                talk("Playing " + song + ' by ' + artist)
            else:
                talk("Playing " + song)
            pywhatkit.playonyt(search_query)

        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + current_time)

        elif 'question' in command:
            talk("Yes, what is your question?")
            question = take_command() 
            info = wikipedia.summary(question, 1)   
            talk(info)
        
        elif 'how are you' in command:
            talk(how_are_you_response())

        elif 'joke' in command:
            talk(pyjokes.get_joke())    

        else:
            talk('I didnt get you')    

run_nova()