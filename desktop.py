# importing modules
from typing import Text
import pyttsx3
import speech_recognition as sr
import datetime as dt
from time import *
import wikipedia
import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from keyboard import *
import pandas as pd
import speedtest


from features import *
# os.startfile("kuch.pyw")


# setting speak engine
eg = pyttsx3.init('sapi5')
voices = eg.getProperty('voices')
eg.setProperty('voice', voices[0].id)
rate = eg.getProperty('rate')
eg.setProperty('rate', 180)


# Speaking function
def speak(text):
    eg.say(text)
    eg.runAndWait()

# wish function


def wishme():
    hour = int(dt.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning sir")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")

    speak("I am Your assistant, How may i help you")

# listening function


def listen():
    rec = sr.Recognizer()
    rec.energy_threshold = 0
    rec.pause_threshold = 2
    with sr.Microphone() as source:
        print("Listening")
        audio = rec.listen(source, timeout=None, phrase_time_limit=4)

    try:
        print("Recognizing")
        query = rec.recognize_google(audio, language='en-in')
    except:
        query = listen()

    return query.lower()


# main execution functions
def main():
    speak("Starting...")
    query = listen()
    print(query)

    if (("hey dad" in query) or ("wake up" in query)):

        wishme()
        query = listen()
        print(query)
        while (('quit' not in query) or ('bye' not in query)):

            if "wikipedia" in query:
                try:
                    query = query.replace("wikipedia", "")
                    print(wikipedia.summary(query, sentences=2))
                    speak(wikipedia.summary(query, sentences=2))

                except wikipedia.exceptions.PageError:
                    speak("Nothing found related"+query)
                except:
                    speak("please repeat again")

            elif 'open youtube' in query:
                speak("opening youtube")
                # webbrowser.open("youtube.com")
                driver = webdriver.Chrome(
                    r"D:\VS CODE\Project\main.py\automation\chromedriver.exe")
                driver.get("http://www.Youtube.com")
                speak("Now, what sir!")
                query = listen()

                if 'search' in query:
                    query = query.replace('search', '')
                    speak("Searching sir")
                    print("Searching sir")
                    s = driver.find_element_by_class_name(
                        "ytd-searchbox").click()
                    write(query)
                    press("Enter")

            elif 'open google' in query:
                speak("opening google")
                webbrowser.open("google.com")

            elif 'open chrome' in query:
                speak("opening chrome")
                os.startfile('chrome')

            elif 'open cu ims' in query:
                webbrowser.open("uims.cuchd.in")

            elif 'open outlook' in query:
                webbrowser.open(
                    "https://outlook.office365.com/mail/inbox/id/AAQkAGYwOGYzNzc1LWJmMjMtNGU1Zi05ZDcyLTkyODQ4N2EzY2RhYQAQAPlhc1CJZblMhIY7pGyE9Bo%3D")

            elif 'open blackboard' in query:
                webbrowser.open("cuchd.blackboard.com")

            elif 'open gmail' in query:
                webbrowser.open("gmail.com")

            elif 'open amazon' in query:
                webbrowser.open('amazon.com')

            elif 'open flipkart' in query:
                webbrowser.open('flipkart.com')

            elif 'play music' in query:
                dir = 'C:\\Users\\R D\\Music\\Attitude'
                song = os.listdir(dir)
                os.startfile(os.path.join(dir, song[1]))

            elif 'the time' in query:
                speak(dt.datetime.now().strftime("%H:%M:%S"))

            elif 'open vs code' in query:
                os.startfile(
                    "C:\\Users\\R D\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk")

            elif (("send mail" in query) or ("send email" in query)):
                try:
                    speak("Write your email id in the column below")
                    mailid = input("Email id : ")
                    speak("Write the password of your mail account below")
                    password = input("Password")

                    speak("To whom you want to send the email")
                    to = input("Receiver mail id : ")
                    speak("What should i write in email to " + to)
                    content = listen()

                    email(to, content)
                    speak("Email sent successfully")

                except Exception as e:
                    print(e)
                    speak("There is some error")

            elif 'quit' in query:
                speak("OK, see you later master")
                main()

            elif 'open calculator' in query:
                os.startfile('calc')

            elif 'open powerpoint' in query:
                os.startfile('powerpnt')

            elif (('open ms word' in query) or ('open word' in query)):
                os.startfile('winword')

            elif (('open notepad' in query) or ('open notes' in query) or ('open note' in query)):
                os.startfile('notepad')

            elif (('open ms excel' in query) or ('open excel' in query)):
                os.startfile('excel')

            elif ('chat' in query) or ('whatsapp' in query) or ('send message' in query) or ('call' in query):
                whatsapp(query)

            elif (('open zoom' in query) or ('open meetings' in query)):
                os.startfile(os.path.join(
                    "C:\\Users\\R D\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Zoom\\Zoom.lnk"))

            elif 'open onenote' in query:
                os.startfile('onenote')

            elif 'volume' in query:
                os.startfile('sndvol')

            elif 'open task manager' in query:
                os.startfile('taskmgr')

            elif (('open file manager' in query) or ('open explorer' in query)):
                os.startfile('explorer')

            elif (('open command prompt' in query) or ('open command' in query)):
                os.startfile('cmd')

            elif (("what's your name" in query) or ("your name" in query)):
                speak("My name is not yet decided, I am in under construction")

            elif ("secret" in query):
                secret()

            elif (("set a reminder" in query) or ("set reminder" in query)):
                remind()

            elif ("speed test" in query) or ("test internet speed" in query) or ("check internet speed" in query) or ("what's my net speed" in query) or ("what's my internet speed" in query):
                speak("checking sir")
                speak("please wait for a while...")
                speed = speedtest.Speedtest()
                upload = speed.upload()
                ups = int(int(upload)/800000)
                down = speed.download()
                dws = int(int(down)/800000)

                print(f"Downloading speed = {dws} MBPS")
                speak(f"sir, your Downloading speed is {ups} M B P S")
                print(f"Uploading speed = {ups} MBPS")
                speak(f"And uploading speed is {dws} M B P S")

            elif ("calculate" in query) or ("what's " in query):
                calculator(query)

            elif ("temperature" in query) or ("weather" in query):
                temp(query)

            else:
                speak("It's not yet coded, Try something else")

            query = listen()

        else:
            speak("ok, See you later sir!")
            query = listen()
            print(query)

    else:
        main()


main()
