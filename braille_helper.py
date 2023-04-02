import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound


#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
# Record Audio


def speak_first(text):


     tts = gTTS(text=text, lang='ko')


     filename='start.mp3'


     tts.save(filename)


     playsound.playsound(filename)
speak_first("단어 말하기")


r = sr.Recognizer()


with sr.Microphone() as source:
    audio = r.listen(source)


# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio,language='ko-KR'))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


def speak(text):


     tts = gTTS(text=text, lang='ko')


     filename='voice.mp3'


     tts.save(filename)


     playsound.playsound(filename)
speak("말씀하신 단어는 " + r.recognize_google(audio,language='ko-KR')+" 맞습니까?")