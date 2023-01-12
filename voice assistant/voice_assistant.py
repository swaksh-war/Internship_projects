import speech_recognition as sr
import playsound
from gtts import gTTS
import os
from selenium import webdriver

num = 1
def assistant_speaks(output):
    global num

    num += 1
    print('PerSon : ', output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    file = str(num)+'.mp3'
    toSpeak.save(file)
    playsound.playsound(file, True)
    os.remove(file)

def get_audio():
    rObject = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        print('Speak...')
        audio = rObject.listen(source, phrase_time_limit=5)
    print('Stop.')

    try:
        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text
    except:
        assistant_speaks("Could not understand your audio, Please try again !")

def open_application(input):
    assistant_speaks("Opening app for you")



def process_text(input):
    try:
        if 'open' in input:
            open_application(input)
    except:
        pass