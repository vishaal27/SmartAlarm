from datetime import datetime
from espeak import espeak
import os
import time
import speech_recognition as sr
current=str(datetime.now())
print(current)
current_time=current[11:19]
current_date=current[:10]
print(current_time)
print(current_date)
#os.system('say '+current_time)
espeak.synth(current_time)
#os.system('say '+current_date)
r=sr.Recognizer();
x=input()
if(x=='x'):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
    	#r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    print('l')
user=r.recognize_google(audio)
print(user)
user=user.lower()
if(user=='alarm' or user=='hallo' or user=='hello' or user=='set' or user=='check' or user=='sad' or user=='state' or user=='side' or user=='check alarm' or user=='set an alarm' or user=='set alarms' or user=='set alarm'):
    #os.system('say "What time should I set the alarm to"')
    espeak.synth("What time should I set the alarm to?")
    time.sleep(5)