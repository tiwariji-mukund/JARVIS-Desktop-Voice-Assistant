import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
from datetime import timedelta
from datetime import datetime

# start engine property
engine = pyttsx3.init("sapi5")
# providing voice to the ssistant
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
# setting the rate of voice
engine.setProperty("rate", 200)


# talk to the user through device's speaker
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# take command from the user through device'c microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}\n")
        except Exception as e:

            return "None"
        return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))

def send_message():
    speak("Whom do you want to message, sir")
    print("1 - Me\n2 - Papa")

    a = int(input("Enter your choice: "))

    if a == 1:
        speak("What is the message to send, sir")
        message = str(input("Enter the message: "))
        pywhatkit.sendwhatmsg("+919451721374", message, time_hour = strTime, time_min = update)


    elif a == 2:
        speak("What's the message")
        message = str(input("Enter the message: "))
        pywhatkit.sendwhatmsg("+919452446211", message, time_hour=strTime, time_min=update)