import requests
import json
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

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Recognising...")
        query  = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print()
        return "None"
    return query



def latestNews():
    apidict = {
        "top headlines" : "https://newsapi.org/v2/top-headlines?country=in&apiKey=f0acff549fdd4964a3b19eccfa93087f",
        "politics" : "https://newsapi.org/v2/top-headlines?country=in&apiKey=f0acff549fdd4964a3b19eccfa93087f",
        "international" : "https://newsapi.org/v2/everything?q=tesla&from=2022-08-23&sortBy=publishedAt&apiKey=f0acff549fdd4964a3b19eccfa93087f",
        "business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=f0acff549fdd4964a3b19eccfa93087f",
        "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=f0acff549fdd4964a3b19eccfa93087f",
        "science" : "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=f0acff549fdd4964a3b19eccfa93087f",
        "sports" : "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=f0acff549fdd4964a3b19eccfa93087f",
        "tech crunch" : "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=f0acff549fdd4964a3b19eccfa93087f",
        "technology" : "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=f0acff549fdd4964a3b19eccfa93087f",
        "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=f0acff549fdd4964a3b19eccfa93087f",
        "google news" : "https://newsapi.org/v2/everything?q=bitcoin&from=2022-08-23&sortBy=publishedAt&apiKey=f0acff549fdd4964a3b19eccfa93087f",
        "tesla" : "https://newsapi.org/v2/everything?q=tesla&from=2022-08-24&sortBy=publishedAt&apiKey=f0acff549fdd4964a3b19eccfa93087f",
        "apple" : "https://newsapi.org/v2/everything?q=apple&from=2022-09-23&to=2022-09-23&sortBy=popularity&apiKey=f0acff549fdd4964a3b19eccfa93087f",
        "google news" : "https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=f0acff549fdd4964a3b19eccfa93087f",
        "finance" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=f0acff549fdd4964a3b19eccfa93087f"
        }

    content = None
    url = None
    speak("Which field news do you want, sir")
    field = takeCommand()
    for key,value in apidict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            break

        else:
            url = True
    if url is True:
        print("url is not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("here is the first news.")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        speak("do you wish to listen more news, sir")
        print("[Speak Yes to continue] and [No to stop]")

        a = takeCommand()

        if str(a) == "yes":
            pass
        elif str(a) == "no":
            break

    speak(f"that's all from {field} news, sir")