
import speech_recognition as sr
import pyttsx3

tts = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print(f"AI: {text}")
    tts.say(text)
    tts.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        response = recognizer.recognize_google(audio)
        print(f"User: {response}")
        return response
    except:
        print("Sorry, couldn't understand.")
        return ""
