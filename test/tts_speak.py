
import playsound
from gtts import gTTS


def speak(text):
     tts = gTTS(text=text, lang='ko')
     filename='voice.mp3'
     tts.save(filename)
     playsound.playsound(filename)
     playsound.close





speak("안녕하세요. 길동씨")