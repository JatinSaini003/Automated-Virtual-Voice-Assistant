import speech_recognition as sr
from os import path

file='D:\\VS CODE\\Project\\main.py\\audio.wav'

r=sr.Recognizer()
with sr.AudioFile(file) as source:
    audio=r.record(source)

try:
    print(r.recognize_google(audio))
except:
    print("no")