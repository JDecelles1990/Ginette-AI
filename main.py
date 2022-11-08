import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import pylint
import random
import time
from time import ctime
#import pyObjC

r = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print('Vous dites nymportekwuh poure muh maylhanger.')
        except sr.RequestError:
            print('No! That is not my problem.')
        return voice_data

