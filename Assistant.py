#!/usr/bin/python

import speech_recognition, wolframalpha, requests, pyperclip
import os, random, time, webbrowser, sys, subprocess, inspect
from pyHS100 import SmartPlug, SmartBulb
from pprint import pformat as pf
# import textIT		#Coming Soon




#-----------------NOT FINISHED YET-------------------#
# def findNumber(name):
# 	ans = helpers.findContact(name)
# 	print(ans)	

#-----------------Misc--------------------#
def getPath():
	p = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	p +="/"
	return p

#-------------------ALARM----------------------#
def calculateTime(text):
	base = int(text[0])
	if (text[1] == 'seconds' or text[1] == 'second'):
		base = base*1
	elif (text[1] == 'minutes' or text[1] == 'minute'):
		base = base*60
	elif (text[1] == 'hours' or text[1] == 'hour'):
		base = base*3600
	return str(base)

def setAlarm(text):
	path = getPath()
	path += 'alarm.py'
	subprocess.Popen(["nohup", "python3", path, text])
	
#-----------------REMINDERS--------------------#
	
def cleanReminders():
	path = getPath()
	path += "reminders.txt"
	file = open(path, "w")
	file.write(" ")
	file.close()

def makeReminder(text):
	path = getPath()
	path += "reminders.txt"
	file = open(path, "a")
	file.write("\n"+text)
	file.close()

def readThemReminders():
	path = getPath()
	path += "reminders.txt"	
	file = open(path, "r")
	text = file.readlines()
	for line in text:
		speak(line)

#-----------------TEXT CLEANUP--------------------#
def cleanAlarm(text):
	del text[0]
	del text[0]
	del text[0]
	if (text[0] == 'for'):
		del text[0]
	ans = calculateTime(text)
	return ans

def cleanReminder(text):
	del text[0]
	del text[0]
	del text[0]
	if (text[0] == "that" or text[0] == "to" or text[0] == "for"):
		del text[0]
	this = ' '.join(str(e) for e in text)
	return this
	
def makeItPretty(text):
	del text[0]
	if (text[0] == 'for' or text[0] =='me'):
		del text[0]
	this = ' '.join(str(e) for e in text)
	this = this.replace(" ", "+")
	return this
	
def fixText(text):
	this = ' '.join(str(e) for e in text)
	return this
	
def speak(text):
	os.system("say -v Ava '"+text+"'");

#-----------------WOLFRAM ALPHA API--------------------#

def wolframThisShit(search):
#	app_id = ""   #Put wolfram API here
	client = wolframalpha.Client(app_id)
	res = client.query(search)
	answer = next(res.results).text
	return answer

#-----------------PERSONALIZATION--------------------#

def whatsMyName():
	path = getPath()
	path += "name.txt"
	file = open(path,"r")
	name = file.readline()
	return name
	
def changeName(text):
	path = getPath()
	path += "name.txt"
	os.system('rm -rf name.txt')
	file = open(path, "w")
	file.write(text)
	file.close()
	return text
	
def getGreeting():
	greetings = ["hello", "good morning", "how can i help you", "how are you today", "what do you need assistance with", "how may i assist you", "did you need something", "hi sir how can i help", "ready to help"]
	return random.choice(greetings)
#-----------------LIGHT CONTROL--------------------#

def lights(x):
#	bulb = SmartBulb("") #Put the internal ip of your smart bulb
	bulb.state = x


#-----------------MUSIC CONTROL--------------------#

def playThatFunkyMusic():
	print('Playing Music')
# 	os.system('open ~/Desktop') #Put the location of your playlist file
	
#-----------------DONT TOUCH THIS--------------------#	
def listen():
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)

	try:
	# 		return recognizer.recognize_sphinx(audio)
		return recognizer.recognize_google(audio)
	except speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))
	return ""
	
#-----------------QUESTION & ANSWER--------------------#
def doSomething(theType):
	word = ""
	while (word != "sleep" and word != "go to sleep" and word != "goodbye" and word != "bye"):
		print('listening...')
		if (theType == 'talk'):
			speak(getGreeting())
			word = listen()
		elif (theType == 'text'):
			word = input('>')
		find = word.split()
		## No empty inputs allowed
		if (find == ""):
			find[0] = "badinput"
		print(word)
	
	
		#---------------------SPECIFIC ANSWERS----------------------#
		if (find == "badinput" or word == ""):
			speak("I didnt quite catch that")
		elif (word == "hi"):
			name = whatsMyName()
			speak('Hello '+name)
		elif (word == "goodbye" or word == "bye" or word == "go to sleep" or word == "sleep"):
			speak('bye sir')
		elif (word == "what is my name"):
			name = whatsMyName()
			speak("Your name is "+name)
		elif (find[0] == "call" and find[1] == "me"):
			name = changeName(find[2])
			speak("From now on I will call you "+name)
		elif (word == "how are you"):
			speak('i am fine what about you')
		elif (word == "turn on the lights" or word == "turn the lights on" or word == "lights on"):
			speak('lights are on now')
			lights('ON')
		elif (word == "turn off the lights" or word == "turn the lights off" or word == "lights off"):
			lights('OFF')
			speak('good night')
		elif (word == "what time is it" or word == "what is the time"):
			speak(time.strftime("%X"))
		elif (word == "what is the date" or word == "give me the date"):
			speak(time.strftime("%x"))
		elif (word == "flip a coin"):
			ans = wolframThisShit("flip a coin")
			speak ("This time it is "+ans)
		elif (word == "play music" or word == "play some music" or word == "start playing music" or word == "play my songs"):
			speak("Yes sir")
			playThatFunkyMusic()
		elif (word == "read this" or word == "read all this"):
			speak(pyperclip.paste())
		elif (find[0] == "remind"):
			text = cleanReminder(find)
			makeReminder(text)
			speak("Reminder is saved")
		elif (find[0] == "make" and find[1] == "a" and find[2] == "reminder"):
			text = cleanReminder(find)
			makeReminder(text)	
			speak("Reminder is saved")
		elif (word == "clean my reminders" or word == "delete my reminders" or word == "clear my reminders" or word == "clear all reminders" or word == "clear reminders" or word =="clean all reminders"):
			cleanReminders()
			speak("Reminders are cleared")
		elif (word == "read my reminders" or word == "read the reminders" or word == "reminders"):
			readThemReminders()
# 		elif (find[0] == "text"):   #coming soon
# 			person = find[1]
# 			message = input('What do you want me to say')
# # 			number = findNumber(person)
# 			number = input('Phone number')
# 			textIT.sendText(number, message)
# 			print("Message SENT")
		elif (find[0] == 'set'):
			if(find[1] == 'an' or find[1] == 'a' or find[1] == 'alarm' or find[1] == 'timer'):
				if(find[2] == 'alarm' or find[2] == 'timer' or find[2] == 'for'):
					realTime = cleanAlarm(find)
					setAlarm(realTime)
					speak('Timer is set')
			
			
			
			
		#----------------------GENERAL ANSWERS-------------------------#
		elif (find[0] == "show"):
			search = makeItPretty(find)
			webbrowser.open("https://www.google.com/search?q="+search+"&source=lnms&tbm=isch&sa=X")
		elif (find[0] == "how" or find[0] == "who" or find[0] == "what"):
			search = fixText(find)
			ans = wolframThisShit(search)
			speak(ans)
		elif (find[0] == "search" or find[0] == "find" or find[0] == "look"):
			search = makeItPretty(find)
			webbrowser.open("https://google.com/search?q="+search)
		else:
			speak("I dont know how to respond to that")
		
	
		
	
	
#---------------------------MAIN---------------------------#
recognizer = speech_recognition.Recognizer()
theType = str(sys.argv)
if (len(sys.argv) < 2):
	theType = 'talk'
else:
	if (sys.argv[1] == 'talk'):
		theType = sys.argv[1]
	elif ( sys.argv[1] == 'text'):
		theType = sys.argv[1]
while(1):
	print('Waiting for NAME...')
	if (theType == 'talk'):
		check = listen()
	elif (theType == 'text'):
		check = input(">")
	print(check)
	if (check == "JARVIS" or check == "jarvis"): #Put the name trigger for your assistant here
		doSomething(theType)
		
		
