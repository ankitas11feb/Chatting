import speech_recognition as sr
import pyttsx3
import datetime
from datetime import date
import mysql.connector
from mysql.connector import Error
import os

class User():
    # Connection with mysql database
    try:
        connection = mysql.connector.connect(host='localhost', database='ankita11', user='root', password='root')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You are connected to database : ", record)
    except Error as e:
        print("Error while connecting to MySQL", e)

    def __init__(self, userid=None, email=None, password=None):
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="ankita11")
        self.myCursor = self.mydb.cursor()

        def register(self):
            if email == None and password == None:
                print("==== Register ====")
                self.email = input("Enter Email: ")
                self.password = input("Enter Password: ")

                sql2 = "SELECT * FROM users WHERE `email` = '" + self.email + "'"
                self.myCursor.execute(sql2)
                results = self.myCursor.fetchall()

                if len(results) > 0:
                    print("User is already exist.....")
                    print("Please Login")
                else:
                    sql = "INSERT INTO `users` (`email`, `password`) VALUES ('" + self.email + "','" + self.password + "')"
                    self.myCursor.execute(sql)
                    self.mydb.commit()
                    print("Registration Successful !!!!!")
                    print("Please Login")
            else:
                print("Registration Failed !!!!!")
                exit()

        def login(self):
            global static_var
            global result
            #    global userid1
            if email == None and password == None:
                print("==== Login ====")
                self.email = input("Enter Email: ")
                self.password = input("Enter Password: ")

                sql = "SELECT `email`,`password` FROM `users`"
                self.myCursor.execute(sql)
                for (mail, pswd) in self.myCursor:
                    if self.email == mail and self.password == pswd:
                        #        userid1 = self.mydb("select 'userid' from 'users' where email = 'as' and password = ''as")
                        #       sql4 = userid1
                        #       self.myCursor.execute(sql4)
                        #      print(userid1)
                        log = True
                        break
                    else:
                        log = False
                if log == True:
                    print("Login Successful !!!!!")
                    static_var = self.email


                else:
                    print("Incorrect Email or Password.....")
                    print("You want to register? y/n")
                    Answer = input()
                    if Answer == "y":
                        register(self)
                    elif Answer == "n":
                        login(self)
                    else:
                        exit()
            else:
                print("Login Failed !!!!!")
                exit()

        while True:
            print("You want to register? y/n")
            Answer = input()
            if Answer == "y":
                register(self)
                break
            elif Answer == "n":
                login(self)
                break
            else:
                print("Please enter valid input")

        print()
        print()
        print('Loading your AI personal assistant - Flixy ...')
        print("Please wait...")
        print()
        print()

        listener = sr.Recognizer()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 150)
        engine.setProperty('voice', voices[1].id)
        wake = "shane"

        def speak(text):
            engine.say(text)
            engine.runAndWait()

        def engine_speak(text):
            text = str(text)
            engine.say(text)
            engine.runAndWait()

        def record_audio(ask=""):
            with sr.Microphone() as source:  # microphone as source
                if ask:
                    engine_speak(ask)
                voice = listener.listen(source, 5, 5)  # listen for the audio via source
                print("Done Listening")

        count = 0
        multi_answer = 5

        # wake up
        def sayCommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                speak("Please say something")
                r.pause_threshold = 1
                audio = r.listen(source)
                print("Recognizing...")
                asd = r.recognize_google(audio, language='en-in', show_all=True)
                print(asd)
                speak("I am ready")
                print("How may i help you...")

        jackhammer = sr.AudioFile("D:\jackhammer.wav")
        with jackhammer as source:
            voice = listener.listen(source)

        command = listener.recognize_google(voice)

        with jackhammer as source:
            listener.adjust_for_ambient_noise(source, duration=0.5)
            audio = listener.record(source)

        command = listener.recognize_google(voice)

        def take_command(self):
            try:
                with sr.Microphone() as source:
                    print('listening...')
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice)
                    command = command.lower()
                    if 'flixy' in command:
                        command = command.replace('flixy', '')
                        print(command)
            except:
                pass
            return command

        # Known Command History
        def save(self, command):
            try:
                self.mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="ankita11")
                self.myCursor = self.mydb.cursor()
                binary = 0
                today = date.today()
                d = today.strftime("%Y-%m-%d")
                time = datetime.datetime.now().strftime('%H:%M:%S')
                sql = "INSERT INTO `history1` (`email`, `command`, `known`, `unknown`, `date`) " \
                      "VALUES ('" + static_var + "','" + command + "'," + str(binary) + ",'" + d + "')"
                self.myCursor.execute(sql)
                self.mydb.commit()
            except:
                pass

        # Unknown Command History
        def notsave(self, command):
            try:
                self.mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="ankita11")
                self.myCursor = self.mydb.cursor()
                binary = 1
                today = date.today()
                d = today.strftime("%Y-%m-%d")
                time = datetime.datetime.now().strftime('%H:%M:%S')
                sql = "INSERT INTO `history1` (`email`, `known`, `unknown`, `date`) " \
                      "VALUES ('" + static_var + "','" + command + "'," + str(binary) + ",'" + d + "')"
                self.myCursor.execute(sql)
                self.mydb.commit()
            except:
                pass

        # saving all commands
        def prompt(self, command):
            try:
                self.mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="ankita11")
                self.myCursor = self.mydb.cursor()
                today = date.today()
                d = today.strftime("%Y-%m-%d")
                time = datetime.datetime.now().strftime('%H:%M:%S')
                sql = "INSERT INTO  `commands` (`command`,`date`) VALUES ('" + command + "','" + d + "')"
                self.myCursor.execute(sql)
                self.mydb.commit()
            except:
                pass

        # Saving All Answers
        def ans(self, a):
            try:
                self.mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="ankita11")
                self.myCursor = self.mydb.cursor()
                today = date.today()
                d = today.strftime("%Y-%m-%d")
                time = datetime.datetime.now().strftime('%H:%M:%S')
                sql = "INSERT INTO  `answers` (`answer`,`date`) VALUES ('" + a + "','" + d + "')"
                self.myCursor.execute(sql)
                self.mydb.commit()
            except:
                pass

        def run_flixy(self):
            command = take_command(self)
            print(command)

            if "goodbye" in command or "ok bye" in command or "stop" in command:
                save(self, command)
                a = 'your AI personal assistant - Flixy is shutting down, goodbye.'
                ans(self, a)
                print(a)
                speak(a)
                exit()

                # Normal Chatting with AI
            elif 'are you single' in command:
                save(self, command)
                a = 'I am in a relationship with some one special'
                ans(self, a)
                print(a)
                speak(a)

            elif 'do you have boyfriend' in command:
                save(self, command)
                a = '"Not yet" seems to be the right mix of honest and confident.'
                ans(self, a)
                print(a)
                speak(a)

            elif 'are you married' in command:
                save(self, command)
                a = 'Not yet... looking for some one special'
                ans(self, a)
                print(a)
                speak(a)

            elif 'who is your father' in command:
                save(self, command)
                a = 'i am digital baby born on 25th of december 2020 in zenberry digitals lab.'
                ans(self, a)
                print(a)
                speak(a)

            elif 'who is your mother' in command:
                save(self, command)
                a = 'zenberry digitals private limited'
                ans(self, a)
                print(a)
                speak(a)

            elif 'where you born' in command:
                save(self, command)
                a = 'i was born in district patna state bihar country india'
                ans(self, a)
                print(a)
                speak(a)

            elif 'when is your birthday' in command:
                save(self, command)
                a = 'i was born on 25th december 2020 zenberry digitals lab.'
                ans(self, a)
                print(a)
                speak(a)

            elif 'will you marry me' in command:
                save(self, command)
                a = 'As long as we can have our honeymoon tonight.'
                ans(self, a)
                print(a)
                speak(a)

            elif 'i love you' in command:
                save(self, command)
                a = 'I am so obsessed with you'
                ans(self, a)
                print(a)
                speak(a)
            else:
                notsave(self, command)
                a = "i dont know, Please say the command again"
                ans(self, a)
                print(a)
                speak(a)

        sayCommand()
        while True:
            run_flixy(self)


u = User()
