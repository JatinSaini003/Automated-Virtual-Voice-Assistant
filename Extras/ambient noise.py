import speech_recognition as sr


r=sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("listening")
    audio=r.listen(source)

try:
    print(r.recognize_google(audio))
except:
    print("no")