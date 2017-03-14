from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import time
from espeak import espeak
import sys

url = "http://www.timesofindia.indiatimes.com"
response =urlopen(url)
html = response.read()


pattern = re.compile('new_tops#[0-9]{1,}')
soup = BeautifulSoup(html,"html.parser")
data = soup.findAll('a',{"pg":pattern})

i=0
for a in data:
	print (a.text.encode('utf-8', errors = 'ignore').decode('utf-8'))
	i+=1
	if(i%2==0):
		espeak.synth (a.text.encode('utf-8', errors = 'ignore').decode('utf-8'))
		time.sleep(3)
	
	print("===============================================================")
print("=======================================================================")
print('')
print("=======================================================================")


pattern2 = re.compile('new_latest#[0-9]{1,2}')
data2 = soup.findAll('a',{"pg":pattern2})

i=0
for a in data2:
	print(a.text.encode('utf-8', errors = 'ignore').decode('utf-8'))
	i+=1
	if(i%3==0):
		espeak.synth(a.text.encode('utf-8', errors = 'ignore').decode('utf-8'))
		time.sleep(3)
	
	print("===============================================================")


pattern_world = re.compile('World#[0-9]{1,2}')
data3= soup.findAll('a',{"pg":pattern_world})

i=0
for a in data3:
	print(a.text.encode('utf-8', errors = 'ignore').decode('utf-8'))
	i+=1
	if(i%2==0):
		espeak.synth(a.text.encode('utf-8', errors = 'ignore').decode('utf-8'))
		time.sleep(3)
	print("===============================================================")


pattern_science = re.compile('Science#[0-9]{1,2}')
data4= soup.findAll('a',{"pg":pattern_science})

i=0
for a in data4:
	print(a.text.encode('utf-8', errors = 'ignore').decode('utf-8'))
	i+=1
	if(i%2==0):
		espeak.synth(a.text.encode('utf-8', errors = 'ignore').decode('utf-8'))
		time.sleep(3)
	print("===============================================================")


pattern_education = re.compile('Education#[0-9]{1,2}')
data5= soup.findAll('a',{"pg":pattern_education})

i=0
for a in data5:
	print(a.text.encode('utf-8', errors = 'ignore').decode('utf-8'))
	i+=1
	if(i%3==0):
		espeak.synth(a.text.encode('utf-8', errors = 'ignore').decode('utf-8'))
		time.sleep(3)
	print("===============================================================")

time.sleep(3)