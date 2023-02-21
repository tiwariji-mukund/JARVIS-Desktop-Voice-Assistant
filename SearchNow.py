import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source, 0, 4)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}\n")
        except Exception as e:

            return "None"
        return query

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        speak("working on that, sir")
        query = query.replace("jarvis", "")
        query = query.replace("google search", "")
        query = query.replace("search", "")
        query = query.replace("on", "")
        query = query.replace("google", "")
        query = query.replace("wikipedia", "")
        speak(f"{query}")
        speak("This is what, I found on, Google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 2)
            speak(result)

        except:
            speak("No speakale output available")

def searchYouTube(query):
    if "youtube" in query:
        speak("working on that, sir")
        query = query.replace("jarvis", "")
        query = query.replace("youtube", "")
        query = query.replace("youtube search", "")
        query = query.replace("search", "")
        query = query.replace("on", "")
        web = "https://www.youtube.com/results?search_query=" + query
        speak(f"searching {query} on youtube")
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("This is what i found for your search on youtube")
        speak("Done, sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia...")
        query = query.replace("jarvis", "")
        query = query.replace("wikipedia", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("search", "")
        query = query.replace("on", "")
        results = wikipedia.summary(query, sentences = 2)
        speak("According to wikipedia")
        print(results)
        speak(results)