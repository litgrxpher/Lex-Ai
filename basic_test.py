import pywhatkit
import datetime
import wikipedia
import random
import pyjokes


def talk(text):
    print("Lex: " + text)

def how_are_you_response():
    responses = [
        "I'm doing well, thank you.",
        "I'm fine, thanks.",
        "I'm alright, thanks for asking.",
        "I'm doing okay, just taking things one step at a time.",
        "I'm doing fine, nothing out of the ordinary."
    ]
    return random.choice(responses)

def take_command():
    command = input("You: ").lower()
    return command

def run_lex():
    while True:
        command = take_command()
        if 'hey lex' in command or 'hi lex' in command:
            talk('How can I help you today?')

        elif 'thank you' in command or 'stop' in command:
            talk("Goodbye!")
            break

        elif 'play' in command and ('song' in command or 'me a song' in command):
            talk("Yes, can you tell me the name and artist?")
            song_command = take_command()
            if 'by' in song_command:
                parts = song_command.split(' by ')
                song = parts[0].strip()
                artist = parts[1].strip()
            else:
                song = song_command
                artist = None
            search_query = f"{song} {artist}" if artist else song
            if artist:
                talk(f"Playing {song} by {artist}")
            else:
                talk(f"Playing {song}")
            pywhatkit.playonyt(search_query)

        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + current_time)

        elif 'question' in command:
            talk("Yes, what is your question?")
            question = take_command()
            try:
                info = wikipedia.summary(question, 1)
                talk(info)
            except wikipedia.exceptions.DisambiguationError as e:
                talk("The question is too ambiguous, please be more specific.")
            except wikipedia.exceptions.PageError:
                talk("I couldn't find any information on that.")
            except Exception as e:
                print(e)
                talk("An error occurred while searching for your question.")

        elif 'how are you' in command:
            talk(how_are_you_response())

        elif 'joke' in command:
            talk(pyjokes.get_joke())

        else:
            talk('I didn\'t get you')

run_lex()
