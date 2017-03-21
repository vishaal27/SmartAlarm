import time
import datetime
import urllib.request
from datetime import datetime as dt
from datetime import date
import calendar
from espeak import espeak
from selenium import webdriver
import email
import imaplib
import random
import math
import signal
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import sys
import json

called=True
running=True

jokes_list=[
'0,"Yo mama so fat, I took a picture of her last Christmas and its still printing."',
'1,"What do you get when you cross a lawyer with the Godfather? An offer you cant understand."',
'2,"Yo mama so poor your family ate cereal with a fork to save milk."',
'3,"Why Does Ariel wear seashells? Because she cant fit into D-shells"',
'4,"If I could have dinner with anyone, dead or alive......I would choose alive."',
'5,"Two guys walk into a bar. The third guy ducks."',
'6,"Why cant Barbie get pregnant? Because Ken comes in a different box."',
'7,"Why was the musician arrested? He got in treble."',
'8,"Did you hear about the guy who blew his entire lottery winnings on a limousine? He had nothing left to chauffeur it."',
'9,"What do you do if a bird shits on your car? Dont ask her out again."',
'10,"He was a real gentlemen and always opened the fridge door for me"',
'11,"Telling my daugthers date that she has lice and its very contagious the closer you get to her. *Correct way to parent."',
'12,"What should you do before criticizing Pac-Man? WAKA WAKA WAKA mile in his shoes"',
'13,"Whats the difference between an illegal Mexican and an autonomous robot...? Nothing... they were both made to steal American jobs."',
'14,"What do you call a barbarian you cant see? an Invisigoth."',
'15,"How do you spell Canda? C,eh,N,eh,D,eh"',
'16,"You ever notice that the most dangerous thing about marijuana is getting caught with it?"',
'17,"What did Arnold Schwarzenegger say at the abortion clinic? Hasta last vista, baby."',
'18,"My wife is in a bad mood. I think her boyfriend forgot their anniversary. Way to go, dude. Now we all suffer..."',
'19,"My speech today will be like a mini-skirt. Long enough to cover the essentials but short enough to hold your attention!"',
'20," What does Miley Cyrus eat for Thanksgiving? Twerky! Just kidding... Drugs. She eats drugs."',
'21,"Why do you never see elephants hiding in trees? Cause they are freaking good at it"',
'22,"How did the blonde die raking leaves? She fell out of the tree."',
'23,"That guy is such a douche-bag! Is he single? Maybe I can fix him!  women"',
'24,"My son just got a tattoo of a heart, a spade, a club, and a diamond, all without my permission. I guess Ill deal with him later."',
'25,"What do you call a potato in space? Spudnik"']


def check_kill_process(pstring):
    for line in os.popen("ps ax | grep " + pstring + " | grep -v grep"):
        fields = line.split()
        pid = fields[0]
        os.kill(int(pid), signal.SIGKILL)

def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time


def url_builder(city_id):
    user_api = '3cey8aff6y2271cye0fbxe2806x3131cb2376xxxxx'  # Obtain yours form: http://openweathermap.org/
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    api = 'http://api.openweathermap.org/data/2.5/weather?id='     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

    full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url


def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict


def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
        sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('deg'),
        dt=time_converter(raw_api_dict.get('dt')),
        cloudiness=raw_api_dict.get('clouds').get('all')
    )
    return data


def data_output(data):
    m_symbol = '\xb0' + 'C'
    print('---------------------------------------')
    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'], m_symbol, data['sky'])
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
    print('')
    print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
    print('Humidity: {}'.format(data['humidity']))
    print('Cloud: {}'.format(data['cloudiness']))
    print('Pressure: {}'.format(data['pressure']))
    print('Sunrise at: {}'.format(data['sunrise']))
    print('Sunset at: {}'.format(data['sunset']))
    print('')
    print('Last update from the server: {}'.format(data['dt']))
    print('---------------------------------------')
    #espeak.synth('Hello Vishaal.')
    #time.sleep(2)
    espeak.synth(' The current weather conditions in Delhi are')
    time.sleep(2)
    temp=data['temp']
    espeak.synth('The current temperature is '+str(temp)+'degrees celsius')
    time.sleep(2)
    espeak.synth('The condition of the sky is '+data['sky'])
    time.sleep(2)
    espeak.synth('The maximum temperature in the day is '+str(data['temp_max'])+'degrees celsius')
    time.sleep(2)
    espeak.synth('The minimum temperature in the day is '+str(data['temp_min'])+'degrees celsius')
    time.sleep(2)
    espeak.synth('The relative humidity percentage is '+str(data['humidity']))
    time.sleep(2)
    time.sleep(2)
    time.sleep(2)

if(called):

	try:
		alarm_time=input('What time should the alarm be set to?')
		espeak.synth('Vishaal, what time should I set the alarm to?')
		time.sleep(3)
		alarm_tone=int(input('What is the alarm tone?'))
		espeak.synth('Vishaal, what should be the alarm tone?')
		time.sleep(3)
		if(alarm_tone==1):
			file='/home/Vishaal/Desktop/Music/better.mp3'
		elif(alarm_tone==2):
			file='/home/Vishaal/Desktop/Music/faded.mp3'
		elif(alarm_tone==3):
			file='/home/Vishaal/Desktop/Music/fight.mp3'
		elif(alarm_tone==4):
			file='/home/Vishaal/Desktop/Music/gone.mp3'
		elif(alarm_tone==5):
			file='/home/Vishaal/Desktop/Music/closer.mp3'
		
		espeak.synth('Vishaal, alarm has been set for '+str(alarm_time))
		time.sleep(3)
		espeak.synth('Vishaal, alarm tone is number'+str(alarm_tone))
		while(running):
			current=str(dt.now())
			current_time=current[11:19]
			current_hours=int(current_time[:2])
			current_minutes=int(current_time[3:5])
			ap=''
			if(current_hours==0):
				ap='am'
				current_hours=12
			elif(current_hours>=13):
				ap='pm'
				current_hours-=12
			else:
				ap='am'
			compare=str(current_hours)+str(current_minutes)+ap
			awake=0
			if(compare==alarm_time):
				print('Get Up.It is time')
				print()
				os.system('vlc '+file)
				x=input('Awake or ... zzz zzz zzz?')

				if(x=='awake'):
					check_kill_process('vlc')
					awake=1
			
				espeak.synth('Good Morning Vishaal.')
				time.sleep(3)
				espeak.synth('Here is a joke for you to start off your day in a cheerful mood')
				time.sleep(5)

				ch=random.randint(1,25)
				chosen=jokes_list[ch]
				if(chosen[1]=='0' or chosen[1]=='1' or chosen[1]=='2' or chosen[1]=='3' or chosen[1]=='4' or chosen[1]=='5' or chosen[1]=='6' or chosen[1]=='7' or chosen[1]=='8' or chosen[1]=='9'):
					speak=chosen[4:]
				else:
					speak=chosen[3:]

				print(speak)
				espeak.synth(speak)
				time.sleep(7)
				espeak.synth('Haha. Funny, aint I?')
				time.sleep(4)


				espeak.synth('Here are the weather updates for today, Vishaal')
				time.sleep(3)
				data_output(data_organizer(data_fetch(url_builder(1273294))))


				user="vishaal16119@iiitd.ac.in"
				password=""
				mail=imaplib.IMAP4_SSL('imap.gmail.com')
				(retcode, capabilities)=mail.login(user,password)
				mail.list()
				mail.select("INBOX")
				mail_from_store=[]
				mail_subject_store=[]

				n=0
				(retcode, messages)=mail.search(None,'(UNSEEN)')
				if(retcode=='OK'):
					for num in messages[0].split():
						n+=1
						result,data=mail.fetch(num,'(RFC822)')
						for r in data:
							if(isinstance(r,tuple)):
								o=email.message_from_bytes(r[1])
								print(o['From'])
								print(o['Subject'])
								mail_from_store.append(o['From'])
								mail_subject_store.append(o['Subject'])
								print()
								result,data=mail.store(num,'+FLAGS','\\Seen')


				print(n)
				if(n>=2):
					s='Vishaal, You have '+str(n)+' unread mails       Do you want me to read the names of the senders and the subjects of the mails?'
					espeak.synth(s)
					time.sleep(10)
				elif(n==1):
					s='Vishaal, You have one unread mail       Do you want me to read the names of the senders and the subjects of the mails?'
					espeak.synth(s)
					time.sleep(10)
				else:
					s='Vishaal, You have no unread mails'
					espeak.synth(s)
					time.sleep(10)

				if(n>=1):
					ch=input()
					if(ch=='no'):
						pass
					elif(ch=='yes'):
						for i in range(len(mail_from_store)):
							s1='You have a mail from '+str(mail_from_store[i])+' and the subject is '+str(mail_subject_store[i])
							espeak.synth(s1)
							time.sleep(10)


				espeak.synth('Vishaal, do you want me to read the latest news?')
				time.sleep(3)
				choi=input()
				if(choi=='yes'):
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



	except KeyboardInterrupt:
		running=False
		print('Quitting')
		print()
		espeak.synth('Bye for now.')
		time.sleep(2)





				




			




