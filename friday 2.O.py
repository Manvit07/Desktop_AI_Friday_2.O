import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_time():
    return datetime.datetime.now().strftime("%H:%M")

def get_day():
    return datetime.datetime.now().strftime("%A")

def get_date():
    return datetime.datetime.now().strftime('%d %B %Y')

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Boss!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Boss!")
    else:
        speak("Good Evening Boss!")
    speak("Friday at your service, how may I help you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")                                                              
    except Exception as e:
        speak("Sorry, I didn't hear you properly. Can you please repeat?")
        print("Please say that again...")
        return "none"
    return query.lower()

if __name__ == "__main__":
    wish_me()
    sites = ["https://www.youtube.com/", "https://www.youtube.com/watch?v=YR12Z8f1Dh8&list=PLb0Wdm54HWRx0Itb6yWfuDxMn2AXozmfS",
             "https://mail.google.com/mail/u/0/#inbox", "https://chat.openai.com/", 'E:\my songs',
             "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"]
    
    while True:
        query = take_command()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("Could you please be more specific?")
            except wikipedia.exceptions.PageError as e:
                speak("Sorry, I couldn't find any relevant information.")
            speak("Anything else I can help you with, sir?")

        elif "time" in query:
            speak(f"Sir, the time is {get_time()}")
            speak("Anything else I can help you with, sir?")

        elif 'date' in query:
            speak(f"Sir, today's date is {get_date()}")
            speak("Anything else I can help you with, sir?")
        
        elif 'week day' in query:
            speak(f"Sir, today is {get_day()}")
            speak("Anything else I can help you with, sir?")

        elif 'open youtube' in query:
            speak("Just a second sir, opening YouTube...")
            webbrowser.open(sites[0])
            speak("Here you go sir.")
            speak("Anything else I can help you with, sir?")

        elif 'playlist' in query:
            speak("Yes boss! Lights, camera, and music...")
            webbrowser.open_new_tab(sites[1])
            speak("Anything else I can help you with, sir?")

        elif "music" in query:
            speak("All right boss...")
            music_dir = sites[4]
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Here are some of your most liked songs.")
            speak("Anything else I can help you with, sir?")

        elif 'open google' in query:
            speak("OK sir...")
            path = sites[5]
            os.startfile(path)
            speak("Here you go sir.")
            speak("Anything else I can help you with, sir?")
        
        elif 'mailbox' in query:
            speak("Just a second boss...")
            webbrowser.open_new(sites[2])
            speak("Here you go sir.")
            speak("Anything else I can help you with, sir?")

            
        elif "open chat gpt" in query:
            speak("OK sir, just a second...")
            speak("By the way, I don't like that chat GPT...")
            webbrowser.open_new(sites[3])
            speak("Here it is.")
            speak("Anything else I can help you with, sir?")
        
        elif "friday stop" in query or any(keyword in query for keyword in ["close", "shut down", "sleep"]):
            speak("OK sir, with your permission...")
            speak("Have a nice day sir!")
            exit()
