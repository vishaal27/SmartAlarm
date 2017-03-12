import random
import os
from espeak import espeak
import speech_recognition as sr
import time

def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

def roman2arabic(value):
    total = 0
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    prevValue = 0
    for char in value:
        if values[char] > prevValue:
            total -= prevValue
        else:
            total += prevValue
        prevValue = values[char]
    total += prevValue

    return total

r=sr.Recognizer();
oneques=(str(random.randint(0,20)),'+',str(random.randint(10,30)))

onequesarr=oneques[0]+oneques[1]+oneques[2]

onequesans=eval(str(onequesarr))

#os.system('say '+onequesarr)
espeak.synth(onequesarr)
time.sleep(2)
#t=int(input('input ans'))
#r = sr.Recognizer()
with sr.Microphone() as source:
    #os.system('say "Say something!"')
    espeak.synth("Say Something")
    audio = r.listen(source)
print(r.recognize_google(audio))


t=r.recognize_google(audio)
if(t[0]=='x' or t[0]=='i' or t[0]=='l' or t[0]=='X' or t[0]=='I' or t[0]=='L'):
    t1=roman2arabic(t.upper())

elif(t[0]=='1' or t[0]=='2' or t[0]=='3' or t[0]=='4' or t[0]=='5' or t[0]=='6' or t[0]=='7' or t[0]=='8' or t[0]=='9'):
    t1=int(t)

elif(isinstance(t[0],str)):
    t1=text2int(t.lower())

print(onequesans)
if(t==int(onequesans) or t1==int(onequesans)):
    #os.system('say "next question"')
    espeak.synth("thug  jjbj  bb next question")
    print('sup')
'''twoques=(str(random.randint(0,10)),'*',str(random.randint(0,10)))
twoquesarr=twoques[0]+twoques[1]+twoques[2]
twoquesans=eval(str(twoquesarr))
os.system('say '+twoques[0]+' into '+twoques[2])
t1=int(input('input ans'))
print(t1)
print(twoquesarr)
if(t1==int(twoquesans)):
    os.system('say "next question"')
    print('sup')'''




'''
try:
    print(  r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))'''
