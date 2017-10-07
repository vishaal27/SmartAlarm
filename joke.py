import random
import time
import requests
from espeak import espeak


joke = requests.get('https://api.github.com/user', headers={"Accept": "application/json"}).json()["joke"]

espeak.synth(joke)
time.sleep(7)
espeak.synth('Haha')
time.sleep(3)
