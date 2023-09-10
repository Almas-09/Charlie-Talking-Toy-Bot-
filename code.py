import pyttsx3
import speech_recognition as sr
import winsound
import time
import pyaudio
import datetime
import PyPDF2
import PyPDF2
import PyPDF3
import transformers
import numpy as np
import pywhatkit
import wikipedia
import pyjokes
import random
from playsound import playsound
from gtts import gTTS
import serial



p=pyaudio.PyAudio()



talk = pyttsx3.init()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        Respond("Good Morning Kiddo !")
        port.write(b'h')
  
    elif hour>= 12 and hour<18:
        Respond("Good Afternoon Sweetie !")
        port.write(b'h')
  
    else:
        Respond("Have a pleasant Evening !")
        port.write(b'h')

    Respond("I am your Assistant")
    Respond("What should i call you!!")
    Respond("Tell me your name")
    uname = Listen()
    Respond("Welcome ")
    port.write(b'h')
    Respond(uname)
    port.write(b'u')
    port.write(b'l')
    Respond("How are you feeling")
    pname=Listen()
    if pname=='i am sad':
        Respond("Dont worry every bad day has to come to an end my dear shin chan")
    elif pname=='i am happy':
        Respond("I am glad to know you are happy")
    elif pname=='i am angry':
        Respond("cool down champ take a deep breadth")
    


hi_List = ['hi', 'Hi', 'Hello', 'hello', 'Hey', 'hey', 'yo', 'Yo,','hi charlie', 'Hi charlie', 'charlie', 'charli', 'charle', 'charley', 'honey']
bye_List = ['Bye', 'bye', 'Goodbye', 'goodbye', 'Good bye' 'good bye', 'byebye', 'by by', 'By by', 'Tata', 'tata', 'So long', 'so long', 'okay bye', 'ok bye', 'Ok bye', 'Okay bye']
qst1_list = ["Who are you", 'who are you', 'whats your name', 'your name', 'Your name', 'What are you', 'what are you']
res_neg_list = ['bad robot', 'Bad robot','bad boy', "Bad boy", 'you are rude charlie', 'You are rude charlie', ' you are a bad robot', 'You are a bad robot']
slang_list = ['idiot', 'crap', 'crack pot', 'lusu', 'fool', 'joker']

Love_list = ['i love you', 'I love you', 'Love you', 'love you']
hate_list = ['i hate you', 'I hate you', 'Hate you', 'hate you']
friend = ['who is your best friend', 'best friend' , 'friend']
plays = ['play the song', 'play the video', 'play the rhymes','play','put Wheels on the bus']
sista = ['sister' , 'who is my sister' , 'sista']
joke = ['joke','jokes']
lookleft=['look left','left']
math_quiz =['maths quiz','maths question','mental maths']



try:
    port=serial.Serial('COM6',baudrate=9600,timeout=0.5)
    print("Connected")
except:
    print("No")
def Listen():
    
    speech = sr.Recognizer()
    winsound.PlaySound("*",winsound.SND_ALIAS)
    print("Eager to serve you")
    with sr.Microphone() as source:
        voice = speech.listen(source) 
        text = speech.recognize_google(voice)
        text=text.lower()
        if 'charlie' in text:
            print(text)

    return text



    
def Decide(listen):
    
    print(f" Command = {listen}.")
    
    if listen in hi_List:
        print("Response in Hi list")
        port.write(b'h')
        Respond("Hi there, Good to see you.How can I help you.")
        Respond("Informative or Entertainment")
        port.write(b'u')
        port.write(b'l')
    elif 'informative' in listen:
        Respond("you can get to know about someone by asking for who is the person or you can ask for mental maths")
    elif 'entertainment' in listen:
        port.write(b'u')
        port.write(b'l')
        Respond("do you want me to play any songs ask for play the song charlie.Or if you want me too put you to sleep ask me sing a sleep song ")
        Respond("If you want me to narrate a story say tell story If you want me to say a poem say tell poem If you want me  to tell you a rhyme say tell me a rhyme") 
        return

    elif listen in bye_List:
        print("In bye list.")
        port.write(b'u')
        Respond("I liked talking with you, okay take care.")
        port.write(b'l')

    elif listen in Love_list:
        Respond("Yuk, I have a girl friend.Her name is Let.I'm no longer available")
        port.write(b's')
    
    
    elif listen in hate_list:
        Respond("Hate you too.")
        port.write(b's')
     
    elif listen in qst1_list:
        port.write(b'h')
        Respond("""I am Charlie the bot. The smart talking robot ever written in python.
                    My creator Nisha Let Swetha Almas are trying to make me smart""")
    
    elif listen in res_neg_list:
        Respond("I am very sorry I was just joking.")

    elif listen in slang_list:
        Respond("Dont talk bad words")

    elif listen in friend:
        Respond("My sweet heart is Stivya")

    elif listen in sista:
        Respond("My sister is Valen")

    elif 'play' in listen:
            Respond("Getting things done")
            port.write(b'u')
            song=listen.replace('play','')
            Respond('playing'+song)
            pywhatkit.playonyt(song)
            port.write(b'l')
            port.write(b's')

    elif 'dance party' in listen:
            port.write(b's')
            port.write(b's')
            port.write(b's')
            port.write(b'h')
            playsound('baby shark.mp3')
           

    elif 'punch' in listen:
        port.write(b'p')

    elif 'smash' in listen:
        port.write(b's')

    elif 'uppercut' in listen:
        port.write(b'U')
    elif 'who is' in listen:
        person = listen.replace('who is', '')
        info=wikipedia.summary(person, 1)
        print(info)
        Respond(info)

    elif 'date' in listen:
        date=datetime.datetime.now().strftime('%l:%M%p')
        Respond('Current time is'+time)

    elif 'tell story' in listen:
        with open('tortoise.pdf', 'rb') as book:
            port.write(b's')
            book_read = PyPDF2.PdfReader(book)
            page_list = book_read.pages
            story_page = page_list[0]
            page_text = story_page.extract_text()
            talk.say(page_text)
        talk.runAndWait()

    elif listen in math_quiz:
        Respond("Welcome to Maths quiz")
        port.write(b'U')
        Respond("what operation you want to exercise")
        operation=Listen()
        print(operation)
        number_one = random.randint(1, 9)
        number_two = random.randint(1, 9)
   
        if 'plus' in Listen():
            Respond(number_one)
            Respond(number_two)
            solution = number_one + number_two
            print(solution)
            Respond("Tell me the answer")
            user_solution1=Listen()
            user_solution=int(user_solution1)
            print("CHECK:", user_solution)
            if(user_solution == solution):
                Respond("Your answer is correct")
            else:
                Respond("Incorrect answer")
        elif 'minus' in Listen():
            Respond(number_one)
            Respond(number_two)
            solution = number_one - number_two
            print(solution)
            Respond("Tell me the answer")
            port.write(b'u')
            port.write(b'l')
            user_solution1=Listen()
            user_solution=int(user_solution1)
            if(user_solution == solution):
                Respond("Your answer is correct")
            else:
                Respond("Incorrect answer")
        elif 'into' in Listen():
            Respond(number_one)
            Respond(number_two)
            solution = number_one * number_two
            Respond("Tell me the answer")
            port.write(b'u')
            port.write(b'l')
            user_solution1=Listen()
            user_solution=int(user_solution1)
            if(user_solution == solution):
                Respond("Your answer is correct")
            else:
                Respond("Incorrect answer")
        else:
            Respond(number_one)
            Respond(number_two)
            solution = number_one + number_two
            Respond("Tell me the answer")
            user_solution1=Listen()
            user_solution=int(user_solution1)
            if(user_solution == solution):
                Respond("Your answer is correct")
            else:
                Respond("Incorrect answer")

  
    elif 'tell another story' in listen:
        with open('pig.pdf', 'rb') as book:
            port.write(b's')
            book_read = PyPDF2.PdfReader(book)
            page_list = book_read.pages
            story_page = page_list[0]
            page_text = story_page.extract_text()
            talk.say(page_text)
        talk.runAndWait()
        
    elif 'recite poem' in listen:
        with open('poem.pdf', 'rb') as book:
            port.write(b'u')
            port.write(b'l')
            book_read = PyPDF2.PdfReader(book)
            page_list = book_read.pages
            story_page = page_list[0]
            page_text = story_page.extract_text()
            talk.say(page_text)
        talk.runAndWait()
   
    elif 'tell a rhyme' in listen:
        port.write(b'U')
        playsound('rowyourboat.mp3')

    elif 'sing a sleep song' in listen:
        port.write(b'u')
        playsound('Snowman.mp3')
        port.write(b'l')

    else:
        Respond("Sorry I don't understand Please say again.")



    

def Respond(t):
    print(f"Talking the: {t}") 

    talk.say(t)
    talk.setProperty('rate', 110) 
    talk.runAndWait()



wishMe()
while True: 
    

    comm = Listen() 

    Decide(comm)  

    time.sleep(3) 
