import random
import time
from espeak import espeak
import requests
import pyjokes
import json

# parses the response received from the api to json format
response = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}).json()

# no need to use unneccessary if statements. just a call to pyjoke.
# first parameter for language, second for category. refer docs for more info.
random_adult_joke = pyjokes.get_joke('en','adult')
random_neutral_joke = pyjokes.get_joke()

# get list of jokes for a particular Genre.
chuck_norris_jokes = pyjokes.get_jokes('en','chuck')
                                     
# assigns the gets the joke from the parsed json and assigns to chosen
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
