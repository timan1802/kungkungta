
from gtts import gTTS
import os
import time
import playsound
from io import BytesIO

def speak(text):
     tts = gTTS(text=text, lang='ko')
     filename='voice.mp3'
     tts.save(filename)
     playsound.playsound(filename)
     playsound.close





speak("안녕하세요. 길동씨")