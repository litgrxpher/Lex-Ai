import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""  
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey nova' in command or 'hi nova' in command:
                talk('How can I help you today?')
                
    except Exception as e:
        print(e)
    return command

def run_nova():
    while True:
        command = take_command()
        if 'stop' in command:
            talk("Goodbye!")
            break

        if 'play' in command and ('song' in command or 'me a song' in command):
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

        if 'time' in command:
            time= datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)


run_nova()
