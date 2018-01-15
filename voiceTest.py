import pygame
import speech_recognition as sr
import webbrowser
import subprocess
from twilio.rest import Client
import twilio
from twilio import*
import os
import time
# get audio from the microphone
from weather import Weather
from bs4 import BeautifulSoup
import requests
import urllib
from pygame import mixer

#can be used to send a message using twilio if the user has an account
#note the account present has since expired and does not authenticate
def sendMessage(message):
    account_sid = "AC3ed7cd380fc992f6d95797834b6d8c45"
    auth_token = "8de727dd8da4be8eb92f85c9a70bde36"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+1314620611",
        body=message,
        from_="+13142309468")

#outputs a file with the forecast for the week
def getWeather(area):
    weather = Weather()
    location = weather.lookup_by_location(area)
    condition = location.condition()
    forecasts = location.forecast()
    file = open("weatherFile.txt", "r+")
    for forecast in forecasts:
        string = "forecast:"
        string += str(forecast.text())
        file.write(string)
        file.write("\n")
        string = "date: "
        string += str(forecast.date())
        file.write(string)
        file.write("\n")
        string = "high:"
        string += str(forecast.high())
        file.write(string)
        file.write("\n")
        string = "low:"
        string += str(forecast.low())
        file.write(string)
        file.write("\n")
    file.close()
    webbrowser.open("weatherFile.txt")

#searches google for whatever is specified by the user
def googleSearch():
    url = "https://www.google.com/search?q="
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("What do you want to google:")
        audio = r.listen(source)
    try:
        words = str(r.recognize_google(audio).lower())
        print("searching for:", words)
        pan = words.replace(" ", "+")
        url += pan
        webbrowser.open(url)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

#webscrapes the front page of NPR and displays all of the
#headlines in a file
def getNews():
    url = "https://www.npr.org/sections/news/"
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    count = 0
    newsFile = open("weatherFile.txt", "r+")
    for link in soup.find_all('h2'):
        count = count + 1
        hTag = link.string
        if(count > 8):
            newsFile.write(hTag)
            newsFile.write("\n")
            newsFile.write("\n")
    newsFile.close()
    webbrowser.open("weatherFile.txt")

#plays a 2 second mp3 file
def playSound(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(0)
    time.sleep(2)

#plays a 4 second mp3 file
def longSound(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(0)
    time.sleep(5)

#runs the main feature of the code that actually performs
#various functions
def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        command = str(r.recognize_google(audio).lower())
        print(command)
        if(command == "open youtube"):
            playSound('C:/Users/edwar/Documents/Audacity/opening youtube now.mp3')
            webbrowser.open("https://youtube.com/")
        elif(command == "open school email"):
            playSound('C:/Users/edwar/Documents/Audacity/opening school email.mp3')
            webbrowser.open('https://outlook.office.com/owa/?realm=email.wustl.edu')
        elif(command == "open personal email"):
            playSound('C:/Users/edwar/Documents/Audacity/opening personal email.mp3')
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif(command == "open linkedin"):
            playSound('C:/Users/edwar/Documents/Audacity/opening linked in.mp3')
            webbrowser.open("https://www.linkedin.com/in/edward-bottom-5a8a10136/")
        elif(command == "open 131"):
            playSound('C:/Users/edwar/Documents/Audacity/opening 131.mp3')
            webbrowser.open("http://www.cse.wustl.edu/~cytron/cse131/")
        elif(command == "open my website"):
            playSound('C:/Users/edwar/Documents/Audacity/opening personal website.mp3')
            webbrowser.open("https://edwardbottom.github.io/Moon/")
        elif(command == "log off"):
            playSound('C:/Users/edwar/Documents/Audacity/logging off.mp3"')
            subprocess.call(["shutdown", "-f", "-s", "-t", "60"])
        elif(command == "power down"):
            playSound('C:/Users/edwar/Documents/Audacity/powering down.mp3')
            subprocess.call(["shutdown", "-f", "-r", "-t", "60"])
        elif(command == "open blackboard"):
            playSound('C:/Users/edwar/Documents/Audacity/opening blackboard.mp3')
            webbrowser.open("https://blackboard.wustl.edu/?tab_tab_group_id=_1_1")
        elif(command == "open facebook"):
            playSound('C:/Users/edwar/Documents/Audacity/open facebook.mp3')
            webbrowser.open("https://www.facebook.com/")
        elif(command == "time to practice"):
            playSound('C:/Users/edwar/Documents/Audacity/time to practice.mp3')
            webbrowser.open("https://www.hackerrank.com/dashboard")
        elif(command == "log hours"):
            playSound('C:/Users/edwar/Documents/Audacity/logging hours.mp3')
            webbrowser.open("https://login.wustl.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s1")
        elif(command == "open google"):
            playSound('C:/Users/edwar/Documents/Audacity/opening google.mp3')
            webbrowser.open("https://www.google.com/")
        elif(command == "open spotify"):
            playSound('C:/Users/edwar/Documents/Audacity/play spotify.mp3')
            webbrowser.open("https://open.spotify.com/browse/featured")
        elif(command == "time for yoga"):
            playSound('C:/Users/edwar/Documents/Audacity/namaste day.mp3')
            webbrowser.open("https://www.youtube.com/watch?v=XImjjhPLeuc")
        elif(command == "what's the weather like"):
            playSound('C:/Users/edwar/Documents/Audacity/weather.mp3')
            getWeather('St. Louis')
        elif(command == "google search"):
            playSound('C:/Users/edwar/Documents/Audacity/google searching.mp3')
            googleSearch()
        elif(command == "time to sleep"):
            playSound('C:/Users/edwar/Documents/Audacity/sweet dreams.mp3')
            webbrowser.open("https://www.youtube.com/watch?v=R-dtHOLjZGo")
        elif(command == "send me a message"):
            with sr.Microphone() as source:
                print("What is you message:")
                audio = r.listen(source)
            try:
                # print("You said " + r.recognize_google(audio))
                command = str(r.recognize_google(audio).lower())
                print(command)
                sendMessage(command)
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
        elif(command == "what's going on in the world"):
            playSound('C:/Users/edwar/Documents/Audacity/checking the news.mp3')
            getNews()
        elif(command == "open amazon"):
            playSound('C:/Users/edwar/Documents/Audacity/right on that.mp3')
            webbrowser.open("https://www.amazon.com/")
        elif(command == "open eclipse"):
            playSound("C:/Users/edwar/Documents/Audacity/opening java.mp3")
            webbrowser.open("C:/Users/edwar/AppData/Roaming/Microsoft/Internet Explorer/Quick Launch/User Pinned/TaskBar/eclipsec.lnk")
        elif(command == "open pycharm"):
            playSound("C:/Users/edwar/Documents/Audacity/opening pycharm.mp3")
            webbrowser.open("C:/Users/edwar/Downloads/pycharm-professional-2017.2.4.exe")
        elif(command == "get my schedule"):
            playSound("C:/Users/edwar/Documents/Audacity/open schedule.mp3")
            webbrowser.open("https://acadinfo.wustl.edu/WSHome/Generic.aspx?Type=Class+Schedule&Page=%2fapps%2fClassSchedule%2f")
        elif(command == "give me motivation"):
            longSound("C:/Users/edwar/Documents/Audacity/smartest.mp3")
        elif(command == "tell me about success"):
            longSound("C:/Users/edwar/Documents/Audacity/success.mp3")
        elif(command == "how are you"):
            longSound("C:/Users/edwar/Documents/Audacity/how are you.mp3")
        elif(command == "how do i look"):
            playSound("C:/Users/edwar/Documents/Audacity/how do I look.mp3")
        else:
            playSound('C:/Users/edwar/Documents/Audacity/reprompt.mp3')
            return main()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

#returns a boolean that is true if Margo was summoned
def intro():
    prompt = False
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
        command = str(r.recognize_google(audio).lower())
        #print(command)
        if command == "margo":
            #print("what is it master?")
            playSound('C:/Users/edwar/Documents/Audacity/what is it master.mp3')
            prompt = True
            return prompt
        else:
            return intro()


#hard code that runs the program
if intro() == True:
    main()


