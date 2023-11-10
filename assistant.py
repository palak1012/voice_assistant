# speech recognition install 
# pyttsx3 install (for text to speech conversion)
# install PyAudio
import speech_recognition as sr
import pyttsx3 #to let bot talk
import pywhatkit #powerful package to search yt,google,etc
import datetime
import wikipedia
import pyjokes
 
listener = sr.Recognizer() #will understand your voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

# in try block we are using microphone as a source and speech recognizer to listen to our source
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...') 
            voice = listener.listen(source)
            command = listener.recognize_google(voice) #asking google
            print(command)
    except:
        pass
    return command

def run_bot():
    command = take_command()
    print(command)
    if 'play' in command :
        song = command.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        # I for 12 hr format and p for am pm M for minutes
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is'+ time)
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info) 
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        ('sorry i did not understood please say again')
while True:
    run_bot()