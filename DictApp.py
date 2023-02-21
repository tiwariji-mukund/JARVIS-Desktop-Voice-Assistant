import pyttsx3
import os
import pyautogui
import webbrowser
from time import sleep

# start engine property
engine = pyttsx3.init("sapi5")
# providing voice to the assistant
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
# setting the rate of voice
engine.setProperty("rate", 200)

# talk to the user through device's speaker
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictApp = {
    "command prompt" : "cmd",
    "word" : "winword",
    "excel" : "EXCEL",
    "google chrome" : "chrome",
    "pycharm" : "pycharm64",
    "edge" : "msedge",
    "browser" : "firefox",
    "powerpoint" : "POWERPNT",
    "powershell" : "powershell",
    "one note" : "onenote",
    "media player" : "VLC",
    "sublime text" : "C:\\Program Files\\Sublime Text\\sublime_text"
}

def openAppWeb(query):
    speak("Working on that, sir")
    if ".com" in query or ".co.in" in query or ".org" or ".ac.in" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace("slash", "/")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
        speak(f"Opening {query}")

    else:
        keys = list(dictApp.keys())
        for app in keys:
            if app in query:
                speak(f"Opening {app}")
                os.system(f"start {dictApp[app]}")

def closeAppWeb(query):
    speak("Closing, sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("All tabs are closed, sir")

    elif "to tabs" in query or "2 tabs" in query or "2 tab" in query or "to tab" in query or "too tabs" in query or "too tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs are closed, sir")

    else:
        keys = list(dictApp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictApp[app]}.exe")