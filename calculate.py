import wolframalpha
import pyttsx3
import speech_recognition as sr

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

def WolfRamAlpha(query):
    apikey = "EVX5V8-LE8YAKW2UT"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer

    except:
        speak("Value is not answerable, sir")

def Calculator(query):
    term = str(query)
    term = term.replace("jarvis", "")
    term = term.replace("Jarvis", "")
    term = term.replace("multiply", "*")
    term = term.replace("into", "*")
    term = term.replace("plus", "+")
    term = term.replace("minus", "-")
    term = term.replace("divided by", "/")

    final = str(term)

    try:
        result = WolfRamAlpha(final)
        print(f"{result}")
        speak(f"Sir, the answer is: {result}")

    except:
        speak("Sorry sir, The value is not answerable")