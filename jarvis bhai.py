import pyttsx3
# Python provides an API called SpeechRecognition
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis ")
    #Speed 1 terahertz, memory 1 gigabyte. Tell me how may I help you

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        # query = r.recognize_google(audio, language='hi')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak(f"Sir, what should I search on youtube")
            data = takeCommand().lower()
            webbrowser.open(f"{data}")

        elif 'open google' in query:
            speak(f"Sir, what should I search on google")
            data = takeCommand().lower()
            webbrowser.open(f"{data}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open brave' in query:
            webbrowser.open("brave.com")

        elif 'open classroom' in query:
            webbrowser.open("classroom.google.com")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2\\bin\\pycharm64.exe"
            os.startfile(codePath)


        elif"stop jarvis" in query or "power of jarvis" in query:
            speak("are you sure to quit jarvis")
            data = takeCommand().lower()
            if "yes" in data:
                speak("sir i am going to poweroff see you later Sir")
                exit()
            else:
                break
        elif'how are you' in query:
            # newVoiceRate = 145
            # engine.setProperty('rate', newVoiceRate)
             speak("I am doing fine ")

        elif 'what do you do' in query:
            # newVoiceRate = 145
            # engine.setProperty('rate', newVoiceRate)
            speak('I help you master that is my favorite thing to do ')
