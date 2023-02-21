import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)


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
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


def game_play():
    speak("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    Me_score = 0
    Com_score = 0
    while (i < 5):
        choose = ("rock", "paper", "scissors", "thread")  # Tuple
        com_choose = random.choice(choose)
        query = takeCommand().lower()

        if query == "rock":

            if com_choose == "rock":
                speak("ROCK")
                print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")

            elif com_choose == "paper":
                speak("paper")
                Com_score += 1
                print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")

            elif com_choose == "scissors":
                speak("Scissors")
                Me_score += 1
                print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")

            else:
                speak("thread")
                Com_score += 1
                print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")

        elif query == "paper":
            if com_choose == "rock":
                speak("ROCK")
                Me_score += 1
                print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")

            elif com_choose == "paper":
                speak("paper")
                print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")

            elif com_choose == "thread":
                speak("thread")
                Me_score += 1
                print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")

            else:
                speak("Scissors")
                Com_score += 1
                print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")



        elif query == "scissors" or query == "scissor" or query == "caesar":
            if com_choose == "rock":
                speak("ROCK")
                Com_score += 1
                print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")

            elif com_choose == "paper":
                speak("paper")
                Me_score += 1
                print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")

            elif com_choose == "thread":
                speak("thread")
                Me_score += 1
                print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")

            else:
                speak("Scissors")
                print(f"Score:\nME: {Me_score}\nJARVIS: {Com_score}")

        i += 1

    print()
    print(f"FINAL SCORE:\nME: {Me_score}\nJARVIS: {Com_score}")

    if Me_score > Com_score:
        print("YOU WON THE GAME")
        speak("Congratulation sir, you won the game")

    elif Me_score < Com_score:
        print("JARVIS WON THE GAME")
        speak("Hurray!! I won the game")

    else:
        print("GAME ENDS IN A DRAW!!!")
        speak("That was a nice game, sir")