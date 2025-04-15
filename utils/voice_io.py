# File: utils/voice_io.py
import speech_recognition as sr
import pyttsx3

def speech_to_text():
    """
    Converts spoken input into text using the microphone.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)  # Use Google's STT API
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn’t catch that. Please try again.")
            return None
        except sr.RequestError:
            print("Could not request results from the STT service.")
            return None

from gtts import gTTS
from playsound import playsound
import os

def text_to_speech(text):
    """
    Converts text to speech using Google Text-to-Speech (gTTS).
    """
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")