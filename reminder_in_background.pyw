from numpy.core.arrayprint import _formatArray
import pandas as pd
import datetime as dt
from plyer import notification as nt
import pyttsx3
from time import sleep



r = pd.read_csv('reminder.csv')
hour = list(r['hour'])
min = list(r['min'])
tex = list(r['text'])



eg = pyttsx3.init('sapi5')
voices = eg.getProperty('voices')
eg.setProperty('voice', voices[0].id)
rate = eg.getProperty('rate')
eg.setProperty('rate', 180)


#Speaking function
def speak(text):
    eg.say(text)
    eg.runAndWait()




while True:
    for (p,q) in zip(hour, min):
        print(p,q)
        if ( (dt.datetime.now().hour == p) and (dt.datetime.now().minute == q) ):
            ind_h = hour.index(p)
            ind_m = min.index(q)
            text = tex[ind_m]
            nt.notify(title = text, message=f"sir, it's the time for {text}", app_icon = 'reminder icon.ico', timeout = 10)
            speak(f"Sir, it's the time for {text}")
            sleep(60)
    