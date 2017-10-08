import random
import time
from espeak import espeak
import requests
import json

#parses the response received from the api to json format
response = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}).json()

#assigns the gets the joke from the parsed json and assigns to chosen
chosen=response["joke"]
if(chosen[1]=='0' or chosen[1]=='1' or chosen[1]=='2' or chosen[1]=='3' or chosen[1]=='4' or chosen[1]=='5' or chosen[1]=='6' or chosen[1]=='7' or chosen[1]=='8' or chosen[1]=='9'):
    speak=chosen[4:]
else:
    speak=chosen[3:]
print(speak)
espeak.synth(speak)
time.sleep(7)
espeak.synth('Haha')
time.sleep(3)

