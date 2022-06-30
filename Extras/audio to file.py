import speech_recognition as sr


r=sr.Recognizer()
with sr.Microphone() as source:
    print("listening")
    audio=r.listen(source)

with open("audio.wav", "wb") as f:
    f.write(audio.get_wav_data())