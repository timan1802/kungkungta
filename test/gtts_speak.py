import io
from IPython.display import Audio
from gtts import gTTS

# To play audio text-to-speech during execution
def speak(my_text):
    with io.BytesIO() as f:
        gTTS(text=my_text, lang='en').write_to_fp(f)
        f.seek(0)
        return Audio(f.read(), autoplay=True)

speak("안녕하세요. 길동씨")