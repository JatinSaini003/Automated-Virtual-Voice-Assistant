import pyttsx3
import speech_recognition as sr
import datetime as dt
from time import *
import os
import smtplib
import pandas as pd
import wolframalpha


import reminder
from whatsapp import *



# setting speak engine
eg = pyttsx3.init('sapi5')
voices = eg.getProperty('voices')
eg.setProperty('voice', voices[0].id)
rate = eg.getProperty('rate')
eg.setProperty('rate', 180)


#Speaking function
def speak(text):
    eg.say(text)
    eg.runAndWait()

#listening function
def listen():
    rec = sr.Recognizer()
    rec.energy_threshold = 0
    rec.pause_threshold = 2
    with sr.Microphone() as source:
        print("Listening")
        audio=rec.listen(source, timeout = None, phrase_time_limit=4)

    try:
        print("Recognizing")
        query = rec.recognize_google(audio, language='en-in')
    except:
        query = listen()
    
    return query.lower()

#Email sending function
def email(to, content):
    mailid = ''
    password = ''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(mailid, password)
    server.sendmail(mailid, to, content)
    server.close()

# Reminder function
def remind():
    a=0
    speak("For what you want to set a reminder ? ")
    text = listen()
            
    while (text == ''):
        text = listen()

    else:
        speak("At what time ?")
        t = listen()
        for i in range(0,len(t)):
            if(t[i]==":"):
                a=i
          

        hours =int(t[0:a])+12
        minutes=int(t[a+1:a+3])

        print(t)
        result = reminder.rem(text,t)

        if (result == "done"):
            speak(f"Reminder for {text} is successfully registered")
                    
        else:
            speak(result)
            speak("Try to speak time in like 4:02 p.m. format ")
            t = listen()
            for i in range(0,len(t)):
                if(t[i]==":"):
                    a=i

            t = t.replace("p.m.", "")
            hours =int(t[0:a])+12
            minutes=int(t[a+1:a+3])

            print(t)
            result = reminder.rem(text,t)

            if (result == "done"):
                speak(f"Reminder for {text} is successfully registered")

# API function
def alpha(query):
    key = "QR7TR6-5A2RUYGE7U"
    connect = wolframalpha.Client(key)
    data = connect.query(query)

    try:
        ans = next(data.results).text
        return ans
    except:
        speak(f"No data found related to {query}")

#Calculator function
def calculator(query):
    query = str(query)
    query = query.replace("calculate",'')
    query = query.replace("plus",'+')
    query = query.replace("multiply",'*')
    query = query.replace("minus",'-')
    query = query.replace("divide",'/')
    query = query.replace("into",'*')
    query = query.replace("by",'/')

    result = alpha(query)
    print(result)
    speak(f"{result}")

# Temperature function
def temp(query):
    query = str(query)
    query = query.replace("what's",'')
    query = query.replace("what is the",'')
    query = query.replace("how's",'')
    query = query.replace("how is the",'')

    query = str(query)
    result = alpha(query)
    print(result)
    speak(f"{result}")


def check_name():
    r = pd.read_csv('contacts.csv')
    lst = list(r['name'])

    speak("To whom, sir")
    query = listen()
    query = query.replace("to","")
    global person 
    person = query

    while True:
        if person not in lst:
            speak("This name is not saved in contact list")
            speak("Do i save this in contacts")
            choice = listen()
            if 'yes' in choice:
                speak(f"What's the contact number of {person}")
                num = listen()
                if ("wait" in num):
                    speak("Ok sir, i am waiting")
                    num = listen()
                    while ("write" not in num):
                        num = listen()
                    else:
                        speak("yes sir, what's the number")
                        num = listen()
                        df = pd.DataFrame([[person, num]])
                        df.to_csv('contacts.csv', mode='a', header=False, index=False)
                        speak(f"{person} contact number is successfully saved to our database")
                        sleep(2)
                        break


                else:
                    df = pd.DataFrame([[person, num]])
                    df.to_csv('contacts.csv', mode='a', header=False, index=False)
                    speak(f"{person} contact number is successfully saved to our database")
                    sleep(2)
                    break


            else:
                speak("ok, sir")
                break

        else:
            break


def whatsapp(query):
    os.startfile(os.path.join("C:\\Users\\R D\\AppData\\Local\\WhatsApp\\WhatsApp.exe"))
    sleep(8)

    if ('open whatsapp' in query):
        speak("opened whatsapp, sir")
        query = listen()
    elif ('chat' in query) or ('call' in query) or ('send message' in query) or ('send a message' in query):
        None
    else:
        query = listen()

    while ('close whatsapp' not in query) or ('change tab' not in query):

        if (("send message" in query) or ('send a message' in query)):
            check_name()
            speak(f"what message you want to send to {person}, sir")
            msg = listen()
            while ('' in query):
                query = listen()
            else:
                message(person, msg)
                speak(f"Message sent to {person}, sir")

        elif ('voice call' in query) or ('voice call' in query):
            check_name()
            voice_call(person)

        elif ('video call' in query):
            check_name()
            video_call(person)

        elif ('open chat' in query):
            check_name()
            open_chat(person)

        elif ('write' in query) or ('write message' in query):
            mesg = query.replace('write','')
            mesg = query.replace('write message','')

            if (mesg == '') or (mesg == ' '):
                speak("What message should i write, sir")
                mesg = listen()
                write_msg(mesg)
            else:
                write_msg(mesg)

        elif ('send' in query):
            send()

        elif ('change line' in query):
            change_line()

        elif ('delete message') or ('backspace all' in query) or ('delete' in query):
            del_msg()

        elif ('backspace' in query) or ('delete one word'):
            del_word()




        else:
            write_msg(query)

        query = listen()






