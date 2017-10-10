import random
import time
import requests
from espeak import espeak
import requests
import json

joke = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"}).json()["joke"]

espeak.synth(joke)
time.sleep(7)
espeak.synth('Haha')
time.sleep(3)