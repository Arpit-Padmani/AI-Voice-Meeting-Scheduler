# text_to_speech.py
import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.setProperty('volume', 1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[-1].id)
    engine.say(text)
    engine.runAndWait()
