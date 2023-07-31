import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import os

listener = sr.Recognizer()
enging = pyttsx3.init()
voices = enging.getProperty("voices")
enging.setProperty("voice", voices[1].id)
wake = "Ruby"

# function to cheack if a word is in the input and then do something based on that word 
def talk(input):
    if "play" in input:
        if ("playlist music" in input) or ("music playlist" in input) or ("playlist songs" in input) or ("songs playlist" in input):
            enging.say("opening playlist music")
            enging.runAndWait()
            webbrowser.open("https://www.youtube.com/watch?v=INMbrRjlNKU")
        else:
            enging.say("now playing" + input.replace("play", ""))
            enging.runAndWait()
            pywhatkit.playonyt(input.replace("play", ""))

    elif "time" in input:
        time = datetime.datetime.now().strftime("%H:%M")
        enging.say("The current time is" + time)
        enging.runAndWait()

    elif "date" in input:
        date = datetime.datetime.now().strftime("%B %d %Y")
        enging.say("The current date is" + date)
        enging.runAndWait()

    elif "wikipedia" in input:
        enging.say(wikipedia.summary(input.replace("wikipedia", ""), 1))
        print(wikipedia.summary(input.replace("wikipedia", ""), 1))
        enging.runAndWait()

    elif "open youtube" in input:
        enging.say("opening youtube")
        enging.runAndWait()
        webbrowser.open("https://www.youtube.com/")

    elif "open" in input:
        if ("github" in input) or ("git hub" in input) or ("guitar tab" in input) or ("guitar" in input):
            enging.say("opening github")
            enging.runAndWait()
            webbrowser.open("https://github.com/")
        elif "twitter" in input:
            enging.say("opening twitter")
            enging.runAndWait()
            webbrowser.open("https://twitter.com/")

        elif ("instagram" in input) or ("insta" in input):
            enging.say(" opening instagram")
            enging.runAndWait()
            webbrowser.open("https://www.instagram.com/")
    
        elif "reddit" in input:
            enging.say("opening reddit")
            enging.runAndWait()
            webbrowser.open("https://www.reddit.com/")
    
        elif ("drive" in input) or ("google drive" in input) or ("goggle drive" in input):
            enging.say("opening goggle drive")
            enging.runAndWait()
            webbrowser.open("https://drive.google.com/drive/my-drive")

        elif ("discord" in input) or ("discord app" in input):

        elif ("e-mail" in input) or ("email" in input) or ("gmail" in input):
            enging.say("opening e-mail")
            enging.runAndWait()
            webbrowser.open("https://www.1und1.de/login")

 
    else:
        enging.say(command + input)
        enging.runAndWait()


# funtion called when alexa is said and then it listens for a command and then calls the talk function with the command as a parameter 
def input():
    try: 
        with sr.Microphone() as source:
            print("yes")
            voice = listener.listen(source)
            command = str(listener.recognize_google(voice))
            talk(command.lower())
            print(command)
    except:
        pass


enging.say("Welcome back sir")
enging.runAndWait()
enging.say("all systems are ready")
enging.runAndWait()

#check if Keyword {"Ruby"} is said 
while True:
    try: 
        with sr.Microphone() as source:
            print("listening")
            voice = listener.listen(source)
            command = str(listener.recognize_google(voice))
            if wake in command:
                enging.say("yes?")
                enging.runAndWait()
                input()
    except:
        pass

