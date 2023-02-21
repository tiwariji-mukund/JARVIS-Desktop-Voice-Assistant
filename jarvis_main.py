import pyttsx3
import datetime
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import os
from playsound import playsound
import pyautogui
from time import sleep
from plyer import notification
from pygame import mixer
import pyjokes

#
# '''setting password for our project'''
# for i in range(3):
#     a = input("Enter password to start the program: ")
#     pw_file = open("password.txt", "r")
#     pw = pw_file.read()
#     pw_file.close()
#
#     if (a == pw):
#         print("Welcome! Now give the hot-word command to start the program")
#         break
#
#     elif (i == 2 and a != pw):
#         print("Password input incorrect. Could not load/start the program")
#         exit()
#
#     elif (a != pw):
#         print("Try Again")

# INTRO GIF
from INTRO import play_gif

play_gif

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 170
        audio = r.listen(source, 0, 4)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print()
        return "None"
    return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetUser import greetMe

            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break

                # tell me the time
                if 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    print(strTime)
                    speak(f"Sir, the time is {strTime}")

                # tell me the date
                elif 'date' in query:
                    strDate = datetime.datetime.now().strftime("%m-%d-%Y")
                    print(strDate)
                    speak(f"Sir, the date is {strDate}")

                # normal conversation
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")

                # easy method to open application
                elif "open" in query:
                    query = query.replace("open", "")
                    query = query.replace("jarvis", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                    speak(f"Opening {query}")


                # open and close apps and website
                elif "open" in query:
                    from DictApp import openAppWeb

                    openAppWeb(query)

                elif "close" in query:
                    from DictApp import closeAppWeb

                    closeAppWeb(query)

                # find something on browser
                elif "google" in query:
                    from SearchNow import searchGoogle

                    searchGoogle(query)

                elif "youtube" in query:
                    from SearchNow import searchYouTube

                    searchYouTube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia

                    searchWikipedia(query)

                # news api
                elif "news" in query:
                    from newsRead import latestNews

                    latestNews()

                # youtube controls
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video paused, sir")

                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played, sir")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video Muted, Sir")

                elif "full screen" in query:
                    pyautogui.press("f")

                elif "mini player" in query:
                    pyautogui.press("f")

                elif "normal screen" in query:
                    pyautogui.press("i")

                elif "theatre mode" in query:
                    pyautogui.press("t")

                elif "subtitle" in query:
                    pyautogui.press("c")

                elif "next" in query:
                    pyautogui.hotkey("shift", "n")
                    sleep(0.5)
                    speak("Playing new video, sir")

                elif "previous" in query:
                    pyautogui.hotkey("shift", "p")
                    sleep(0.5)
                    speak("Playing previous video, sir")

                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("Video Un Muted, Sir")

                elif "volume up" in query:
                    from keyboard import volumeUp

                    speak("Turning volume up, sir")
                    volumeUp()

                elif "volume down" in query:
                    from keyboard import volumeDown

                    speak("Turning volume down, sir")
                    volumeDown()

                # make an alarm
                elif "alarm" in query:
                    print("input time example: 10:10")
                    speak("Tell me the time to set the alarm, sir")
                    time = input("Time: ")
                    speak(f"Alarm is set at {time}, sir")

                    while True:
                        time_now = datetime.datetime.now().strftime("%H:%M")

                        if time_now == time:
                            speak("Time to wake up, sir")
                            playsound(r"C:\Users\Mukund\PycharmProjects\Project_Jarvis\Downloads\music.mp3")
                            playsound(r"C:\Users\Mukund\PycharmProjects\Project_Jarvis\Downloads\music.mp3")


                        elif time_now > time:
                            speak("Alarm closed, sir")
                            break

                elif "temperature" in query:
                    search = "temperature at my location"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    print(f"Temperature: {temp}")
                    speak(f"current temperature at your location is {temp}")

                elif "weather" in query:
                    search = "weather today at my location"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    weather = data.find("div", class_="BNeawe").text52
                    print(f"Weather: {weather}")
                    speak(f"current weather at your location is {weather}")

                # making calculator
                elif "calculate" in query:
                    from calculate import WolfRamAlpha
                    from calculate import Calculator

                    query = query.replace("calculate", "")
                    query = query.replace("jarvis", "")
                    Calculator(query)

                # reminder program
                elif "remember that" in query:
                    rememberMessage = query.replace("rememebr that", "")
                    rememberMessage = query.replace("jarvis", "")
                    rememberMessage = query.replace("rememebr", "")
                    rememberMessage = query.replace("that", "")
                    speak("Sir, You told me to  " + rememberMessage)
                    remember = open("remember.txt", "w")
                    remember.write(rememberMessage)
                    remember.close()

                elif "what do you remember" in query:
                    rememebr = open("remember.txt", "r")
                    speak("Sir, You told me to " + rememebr.read())

                # sleep jarvis
                # it would not respond but will listen everything
                elif "break" in query:
                    speak("Ok Sir, You can call me anytime")
                    break

                # shutdown jarvis
                elif "goodbye" in query:
                    speak("Good Bye Sir. Hope we will meet again")
                    exit()


                elif "shutdown" in query:
                    speak("Do you really want to shut down the system, sir")
                    print("0: No")
                    print("1: Yes")
                    shutdown = input("Do you really wish so? (0/1): ")

                    if shutdown == "1":
                        speak("Shutting down the system, sir, good bye")
                        os.system("shutdown /s /t 1")

                    elif shutdown == "0":
                        break

                # change password
                elif "change password" in query:
                    speak("What is the new password, sir")
                    new_pw = input("Enter New Password: ")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Password changed successfully, Sir")
                    print("Password changed successfully")


                # schedule my day function

                elif "schedule my day" in query:
                    tasks = []
                    speak("Do you want to clear old tasks (Yes or No)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open(r"C:\Users\Mukund\PycharmProjects\Project_Jarvis\tasks.txt", 'w')
                        file.write(f"")
                        file.close()

                        no_tasks = int(input("Enter the number of tasks: "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input(f"Enter task {i}: "))
                            file = open(r"C:\Users\Mukund\PycharmProjects\Project_Jarvis\tasks.txt", 'a')
                            file.write(f"{i}. {tasks[i]} \n")
                            file.close()

                    elif "no" in query:
                        no_tasks = int(input("Enter the number of tasks: "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input(f"Enter task {i}: "))
                            file = open(r"C:\Users\Mukund\PycharmProjects\Project_Jarvis\tasks.txt", 'a')
                            file.write(f"{i}. {tasks[i]} \n")
                            file.close()

                # show schedule
                elif "show my schedule" in query:
                    file = open(r"C:\Users\Mukund\PycharmProjects\Project_Jarvis\tasks.txt", 'r')
                    # file = open(r"C:\Users\Ankush\PycharmProjects\Project_Jarvis\tasks.txt", 'r')
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load(r"C:\Users\Mukund\PycharmProjects\Project_Jarvis\Downloads\notification.mp3")
                    # mixer.music.load(r"C:\Users\Ankush\PycharmProjects\Project_Jarvis\Downloads\notification.mp3")
                    mixer.music.play()

                    notification.notify(
                        title="My Schedule:",
                        message=content,
                        timeout=15
                    )

                # cricket score function
                elif "score" in query:
                    url = "https://www.cricbuzz.com/"
                    resp = requests.get(url)
                    soup = BeautifulSoup(resp.content, "html.parser")

                    team1 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()

                    # live match
                    print("Live Match")
                    speak("Live Match")
                    a = print(f"{team1}: {team1_score}")
                    b = print(f"{team2}: {team2_score}")
                    speak(f"Current match is going on between {team1} and {team2}")

                    mixer.init()
                    mixer.music.load(r"C:\Users\Mukund\PycharmProjects\Project_Jarvis\Downloads\notification.mp3")
                    # mixer.music.load(r"C:\Users\Ankush\PycharmProjects\Project_Jarvis\Downloads\notification.mp3")
                    mixer.music.play()

                    notification.notify(
                        title="CURRENT SCORE:",
                        message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout=15,
                    )
                    print()



                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save(r"C:\Users\Mukund\PycharmProjects\Project_Jarvis\ss.jpg")
                    # im.save(r"C:\Users\Ankush\PycharmProjects\Project_Jarvis\ss.jpg")

                # whatsapp automation
                # elif "whatsapp" or "whats app" in query:
                #     from WhatsApp import send_message
                #
                #     send_message()
                #     break

                elif "take a picture" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)

                    speak("Smile Please, sir")
                    pyautogui.press("enter")

                elif "game" in query:
                    from game import game_play

                    game_play()

                elif "joke" in query:
                    get = pyjokes.get_joke()
                    speak(get)

