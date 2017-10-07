import urllib2
import time
import json
import espeak

speak = urllib2.urlopen('http://api.yomomma.info/').read()
speak = json.loads(speak)["joke"]
print(speak)
espeak.synth(speak)
time.sleep(7)
espeak.synth('Haha')
time.sleep(3)
