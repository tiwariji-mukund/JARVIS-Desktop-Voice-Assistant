import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=5 and hour<=12:
        speak("Good Morning,sir")
    elif hour >12 and hour<=16:
        speak("Good Afternoon ,sir")
    else:
        speak("Good Evening,sir")
    speak("I am Jarvis your personal ai assistant, please tell me, How may I help you ?")