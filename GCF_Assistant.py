import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib #pip install smtplib
import random
import pyperclip
import sys
# from googletrans import Translator
email_dict = {"guru": "khannaguru11@gmail.com", "juhi": "29juhi@gmail.com", "rajiv": "khanna.rajiv@gmail.com", "madhuri": "khanna.madhuri@gmail.com"}
jokes = ["What do you call a queue with barbie standing in it?;; a barbeque", "what do you call a person who does not believe in gyms?;; gymnasthik", "where does B come after U?;; when you take some of it's honey", "why was the computer tired when he returned home?;; He had a hard drive", "when does friday come before monday?;; In the dictionary", "why was the computer very tired when it returned home?;; As it had a hard drive", "why did a man having only one hand cross the road?;; because it wanted to go to the second hand shop", "what starts with an E, ends with an E but has only 1 letter in it?;; envelope"]
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

imfine=["I am on cloud 9", "I am amazing, and hope you are too!", "I am fine, thanks for asking!"]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        print("Good Afternoon!")
        speak("Good Afternoon!")   
        

    else:
        print("Good Evening!")
        speak("Good Evening!")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")  
        speak("Recognizing") 
        quer = r.recognize_google(audio, language='en-in')
        print(f"User said: {quer}\n")
        speak(f"you said {quer}\n")
        
        return quer

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        speak("Say that again please...")
        return takeCommand()


wishMe()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kitchenofusha@gmail.com', 'khannajuly24')
    server.sendmail('kitchenofusha@gmail.com', to, content)
    server.close()
        
print("\nI am GCF Assistant.\n\nPlease tell me your name") 
speak("I am gcf assistant. Please tell me your name")      

name = takeCommand()

while True:
    print("\nPress enter to give command")
    speak("Press enter to give command")
    allow = input("")
    
    if allow=="":
        query = takeCommand().lower()
        query = query.replace("'", "")
        # Logic for executing tasks based on query
        if "open wikipedia" in query:
            webbrowser.open("en.wikipedia.org")
        
        elif "quit" in query or "bye" in query or "close" in query:
            print("Have a nice and wonderful day! Bye.")
            speak("Have a nice and wonderful day! Bye")
            sys.exit()

        elif "toss" in query or "flip a coin" in query:
            coinface = ["Heads", "Tails"]
            coinface = coinface[random.randint(1, 2)]
            # playsound("C:\\Users\\khann\\Desktop\\Guru Python\\flappy\\Magic Chime.mp3")
            speak(f"It is {coinface}")
            print(f"It is {coinface}!")
        
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak('Could not search on Wikipedia, you can search for another keyword')

        elif "how are you" in query:
            print("I am fine. Thank you.")
            speak("I am fine. Thank you.")

        elif "search on google" in query:
            print("Tell me what to search on google")
            speak("Tell me what to search on google")
            stext = takeCommand()
            webbrowser.open("https://www.google.com/search?ei=pABGYLDWIsuf9QOl7bHQBQ&q="+stext)

        elif "open amazon" in query:
            webbrowser.open("amazon.in")
            print("\n")

        elif "open powerpoint" in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
            print("\n")
        
        elif "open excel" in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
            print("\n")

        elif "open piano" in query or "open online piano" in query or "open online pianist" in query or "open virtual piano" in query:
            webbrowser.open("onlinepianist.com/virtual-piano")

        elif "open docs" in query or "open google docs" in query:
            webbrowser.open("docs.google.com")

        elif "open word" in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

        elif "open sheets" in query or "open google sheets" in query:
            webbrowser.open("sheets.google.com")

        elif "open slides" in query or "open google slides" in query:
            webbrowser.open("slides.google.com")

        elif "day today" in query or "todays day" in query:
            g = datetime.datetime.now()
            print("Today's day is:\n"+g.strftime("%A"))
            speak("Today's day is:\n"+g.strftime("%A"))

        elif "this month" in query or "the month" in query:
            v = datetime.datetime.now()
            print("The month going on is:\n"+v.strftime("%B"))
            speak("The month going on is:\n"+v.strftime("%B"))

        elif "open gmail" in query:
            webbrowser.open("gmail.com")

        elif "open quizizz" in query:
            webbrowser.open("quizizz.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif "snake water gun" in query:
            os.startfile("C:\\Users\\khann\\Desktop\\Guru Python\\test\\swgg.py")

        elif "open google" in query or "open chrome" in query:
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
        
        elif "open amitranet" in query:
            webbrowser.open("aisg46.amizone.net")
        
        elif "open cult fit" in query or "open cure fit" in query or "open cult" in query:
            webbrowser.open("cure.fit")
        
        elif "type for me" in query:
            print("Tell me what to type")
            speak("Tell me what to type")
            text = takeCommand()
            pyperclip.copy(text)
            print("Text copied to clipboard!")
            speak("Text copied to clipboard!")
        
        elif "open web whatsapp" in query or "open whatsapp" in query:
            webbrowser.open("web.whatsapp.com")
            print("\n")
        
        elif "open vs code" in query or "open visual studio code" in query:
            os.startfile("C:\\Users\\khann\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            print("\n")

        elif "the year" in query or "this year" in query:
            h = datetime.datetime.now()
            print("The year going on is:\n"+h.year)
            speak("The year going on is:\n"+h.year)

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif "my name" in query:
            print("Your name is "+name)
            speak("Your name is "+name)

        elif "open file explorer" in query:
            os.startfile("C:\\Users\\khann\\Desktop\\Apps\\File Explorer.lnk")

        elif "open control panel" in query:
            os.startfile("C:\\Users\\khann\\Desktop\\Apps\\Immersive Control Panel.lnk")

        elif "open new tab" in query:
            webbrowser.open("www.google.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\khann\\Desktop\\fun with apps\\Music\\'
            songs = os.listdir(music_dir)
            # songs=", ".join(songs)
            print(songs)    
            randno = random.randint(0,6)
            os.startfile(os.path.join(music_dir, songs[randno]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(f"The time is {strTime}")   
            speak(f"the time is {strTime}")

        elif 'send email' in query:
            try:
                email_dictionary = str(email_dict.keys())
                email_dictionary = email_dictionary.replace("dict_keys(", "")
                email_dictionary = email_dictionary.replace("'", "")
                email_dictionary = email_dictionary.replace(")", "")
                email_dictionary = email_dictionary.replace("[", "")
                email_dictionary = email_dictionary.replace("]", "")
                print(f"The people available are {email_dictionary}")
                speak(f"The people available are {email_dictionary}")
                speak("to whom should i send the email")
                to = takeCommand().lower()
                toemail = email_dict[to]
                print("What should i say?")
                speak("What should I say?")
                content = takeCommand()    
                sendEmail(toemail, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")

        elif "the date" in query or "todays date" in query:
            x = datetime.datetime.now()
            print("Today's date is:-\n"+x.strftime("%D"))
            speak("Today's date is:-\n"+x.strftime("%D"))

        elif "open new tab" in query:
            webbrowser.open("www.bing.com")

        elif "open vs code" in query or "open visual studio code" in query:
            os.startfile("C:\\Users\\khann\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif "open google" in query or "open chrome" in query:
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            print("\n")

        elif "joke" in query or "riddle"in query:
            joke=jokes[random.randint(0, 6)].capitalize()
            print(f"Here is a joke for you: {joke.replace(';;', '')}")
            speak(f"here is a joke for you: {joke}")
        
        # else:
        #     print("I can not help with that thing. Sorry")
        #     speak("I can not help with that thing. Sorry")