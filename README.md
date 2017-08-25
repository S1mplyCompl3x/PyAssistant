PyAssistant -- JARVIS
===================


**PyAssistant** is a home made customizable voice assistant similar to J.A.R.V.I.S coded in Python made for MacOS (can be adapted for Linux).

## Getting Started

There are 2 ways to run the script:

```
//Voice Activation
Python PyAssistant.py  or  Python PyAssistant.py talk

//Text Activation
Python PyAssistant.py text
```
In text mode you can type all the commands which is mostly used to debug new modules faster.

## Installation

This project was built for Python3 and uses the following libraries:

* [Speech_Recognition](https://pypi.python.org/pypi/SpeechRecognition/) - Library for STT
* [wolframalpha](https://github.com/jaraco/wolframalpha) - WolframAlpha for some questions
* [Pyperclip](https://github.com/asweigart/pyperclip) - Clipboard Control
* [pyHS100](https://github.com/GadgetReactor/pyHS100) - Library to control TP-Link products
* [Cheese](https://apps.ubuntu.com/cat/applications/precise/cheese/) - Webcam as surveillance camera
* [Easymp3](https://github.com/S1mplyCompl3x/easymp3) - Downloading songs made simple

for Linux you need to install:

```
sudo apt-get install gnustep-gui-runtime cheese streamer 

```

You can install the requirements by running pip on the requirements.txt or installing them individually.
A API key from Wolfram Alpha is needed for this project which can be obtained [HERE](https://developer.wolframalpha.com/portal/apisignup.html).

## Usage

PyAssistant runs listening to everything waiting for the trigger word and greets you as soon its heard.
The following are the current commands it can recognize:
> **Usage**

> - **"Hi"** : This greets you with your name
> - **"GoodBye, Bye, Sleep, Go to sleep"** : These kick PyAssistant out of listening mode to idle mode
> - **"Call me (%say name)"** : Changes your predefined name
> - **"Turn the lights on, lights on, lights off, Turn the lights off"** : Turns the selected smart bulb on and off
> - **"What time is it, What is the date"**: Tells the time or the date
> - **"Read this"** : Reads the selected text saved in the clipboard
> - **"Make a reminder to (reminder), Remind me to (reminder)** : Creates a reminder
> - **"Read my reminders, reminders"** : Reads the reminders saved
> - **"Clear my reminders, clear reminders"** : Clears saved reminders
> - **"Set a timer for (time)"** : Set a timer for the said time
> - **"Show me (selected pictures)"** :  Opens the browser and show pictures
> - **"what, how, who (question)"** : Asks wolfram and answer
> - **"Search for (question)"** : searches google for the question
> - **"Turn on the webcam, Webcam on"** : Turns on the webcam and stream it to localhost
> - **"Download (song name)"** : Download the song to current directory
> - **"Read my email, Read mail"** : Read the latest mails from personal email (Add values in readmail.py)
> - And more ...






## License & Final Thoughts

This project is under General Public License, So do whatever you want with this just give me credit, its pretty easy to customize. 

