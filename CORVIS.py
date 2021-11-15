import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from tkinter import *
import time




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as (source):
        print ("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print ("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print (f"user said:\n {query}")

    except Exception as e:
        print ("Sorry, Can't recognize please try again")
        return "None"

    return query
    
def assistant():
        query = takeCommand().lower()
        if 'hi' in query:
            speak("hi")
        elif 'wikipedia' in query:
            print("searching")
            query = query.replace("wikipedia","")
            speak("searching"+query)
            results = wikipedia.summary(query)
            print (results)
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open('https://www.youtube.com')
        elif 'search' and 'youtube' in query:
            query =query.replace("search","")
            query = query.replace("on","")
            query = query.replace("youtube","")
            speak(f"searching {query} on youtube")
            time.sleep(1.0)
            query =query.replace(" ","_")
            
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')

        elif 'open github' in query:
            speak("opening github")
            webbrowser.pen('https://github.com')
        else:
            print("can't find anything")
            speak("can't find anything")
            assistant()

assistant()