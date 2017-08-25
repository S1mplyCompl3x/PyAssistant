#!/usr/bin/env python

import sys, os, re
import imaplib
import email
import email.header
import datetime

EMAIL_ACCOUNT = ""		#Email Address
PASSWD = ""				#Email Password  			
EMAIL_FOLDER = "INBOX"	#Folder to be read

def speak(text):
	os.system("say Ava '"+text+"'");

def process_mailbox(M):
	countIT = 0
	rv, data = M.search(None, "ALL")	#UNSEEN if you want to see unread messages
	if rv != 'OK':
		speak("No messages found!")
		return
	
	for num in reversed(data[0].split()):
		countIT = countIT+1
		if (countIT == 6):
			return
		rv, data = M.fetch(num, '(RFC822)')
		if rv != 'OK':
			print("ERROR getting message", num)
			return

		msg = email.message_from_bytes(data[0][1])
		print('\n')
		temp = 'Message by %s saying %s' % (msg['From'], msg['Subject'])
		line = re.sub('<[^>]+>', '', temp)		#Remove if you want it to say the email address too
		speak(line)

M = imaplib.IMAP4_SSL('imap.gmail.com')	#Mail Server

try:
    rv, data = M.login(EMAIL_ACCOUNT, PASSWD)
except imaplib.IMAP4.error:
    print ("LOGIN FAILED!!! ")
    sys.exit(1)

print(rv, data)

rv, data = M.select(EMAIL_FOLDER)
if rv == 'OK':
    process_mailbox(M)
    M.close()
else:
    print("ERROR: Unable to open mailbox ", rv)

M.logout()