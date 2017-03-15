##### IT - IT'S TIME! by ACMECORPORATION
##### THE RASPBERRY PI STAND ALONE ALARM CLOCK
##### V. 1.3
##### NEW OPTIONS: ON/OFF LED ALARM INDICATOR, 
##### FIXED BACKLIGHT DISPLAY MINIMUM VALUE, FIXED BUG INTRODUCING TIME LIMITATION TO CHOOSE OPTIONS INTO PRIMARY MENU 
#Grove Analog Read sensor example
import time
from grove_rgb_lcd import *
import grovepi
import datetime
from time import strftime
import sys
import os


#Sensor connected to A0 Port 
sensor = 1
button = 3
buzzer = 2
dht_sensor = 4
light_sensor = 0
led = 6
grovepi.pinMode(sensor,"INPUT")
grovepi.pinMode(button,"INPUT")
grovepi.pinMode(buzzer,"OUTPUT")
grovepi.pinMode(light_sensor,"INPUT")
grovepi.pinMode(led,"OUTPUT")

filesveglia = open('/home/pi/sveglia.txt','r')
onoffsveglia = open('/home/pi/onoff.txt','r')
orasveglia = str(filesveglia.readline())
oraonoff = str(onoffsveglia.readline())
filesveglia.close()
onoffsveglia.close()

grovepi.digitalWrite(buzzer,0)


print orasveglia
print oraonoff

def restart_program():
		python = sys.executable
		os.execl(python, python, * sys.argv)

last_sound = 0

while True:
	try:
		[temp,humidity] = grovepi.dht(dht_sensor,0)
		temp = str(temp)
		humidity = str(humidity)
		lsensor_value = grovepi.analogRead(light_sensor)
		lsensor_value = lsensor_value / 2
		if lsensor_value >= 255:
			lsensor_value = 255
		if lsensor_value <= 5:
                        lsensor_value = 5
		print lsensor_value
		giorno = strftime("%d-%m-%Y")
		orario = strftime("%H:%M")
		if oraonoff == "1":
			grovepi.analogWrite(led,lsensor_value)
		else:
			grovepi.analogWrite(led,0)
	    	setRGB(0,0,lsensor_value)
	    	setText(str(giorno + " " + temp + "C\n" + oraonoff + "  *" + orario + "* " + humidity + "%"))
	    	print giorno + orario
	    	if orario == orasveglia and oraonoff == "1":
			onetoten = range(0,5)
		    	for count in onetoten:
				grovepi.digitalWrite(buzzer,0)
				setRGB(200,5,5)
				setText(" W A K E   U P \n   IT'S  " + orasveglia)
				grovepi.digitalWrite(buzzer,1)
				time.sleep(.1)
				setRGB(0,5,5)
				grovepi.digitalWrite(buzzer,0)
				time.sleep(.1)
				setRGB(200,5,5)
				grovepi.digitalWrite(buzzer,1)
				time.sleep(.3)
				setRGB(0,5,5)
				grovepi.digitalWrite(buzzer,0)
				if grovepi.digitalRead(button):
					orario = strftime("%H:%M")
					setRGB(0,0,lsensor_value)
                			setText(str(giorno + " " + temp + "C\n" + oraonoff + "  *" + orario + "* " + humidity + "%"))
                                	time.sleep(60) # snooze time
					onetoth = range(0,3)
					for count in onetoth:
						onetoten = range(0,10)
						for count in onetoten:
                	                		setRGB(200,5,5)
                        	        		setText("  ARE YOU STILL\n   IN BED?")
                                			grovepi.digitalWrite(buzzer,1)
							time.sleep(.1)
							setRGB(0,5,5)
							grovepi.digitalWrite(buzzer,0)
                                                        time.sleep(.1)
							setRGB(200,5,5)
							grovepi.digitalWrite(buzzer,1)
							time.sleep(.2)
							setRGB(0,5,5)
							grovepi.digitalWrite(buzzer,0)
							if grovepi.digitalRead(button):
								restart_program()
                                			time.sleep(.5)
					restart_program()						
				grovepi.digitalWrite(buzzer,0)
				time.sleep(.5)
	    	time.sleep(5)
	    	if grovepi.digitalRead(button):
			time.sleep(1)
			break

        except (IOError,TypeError) as e:
            	print "Error"
		restart_program()
				
#while True:
menu = range(0,10)
for count in menu:
	try:
		sensor_value = grovepi.analogRead(sensor)
		setRGB(20,20,255)
		setText(" < OFF     ON > ")
		time.sleep(0.5)
		onoff = str(int(sensor_value / 512))
		#def restart_program():
		#		python = sys.executable
                #                os.execl(python, python, * sys.argv)
		if onoff == "0" and grovepi.digitalRead(button):
			setText("ALERT OFF")
			onoffsveglia = open('/home/pi/onoff.txt','w')
			onoffsveglia.write("0")
			onoffsveglia.close()
			time.sleep(1)
                        restart_program()
			
		if onoff == "1" and grovepi.digitalRead(button):
                        setText("ALERT ON")
			onoffsveglia = open('/home/pi/onoff.txt','w')
                        onoffsveglia.write("1")
                        onoffsveglia.close()
			time.sleep(1)
			while True:
				try:
					sensor_value = grovepi.analogRead(sensor) 
					setRGB(200,20,255)
					setText(" < SET TIME\n ALREADY DONE > ")
					time.sleep(.5)
					onoff = str(int(sensor_value / 512))
					if onoff == "0" and grovepi.digitalRead(button):
						setRGB(200,20,255)
						setText("    SET HOUR")
						time.sleep(1)
						while True:
				    			try:
								if grovepi.digitalRead(button):
									time.sleep(1)
									selora = str(" SETTED HOUR:\n      " + whour)
									setRGB(0,255,255)
									setText(selora)
									time.sleep(1)
									setRGB(200,20,255)
									setText("   SET MINUTE")
									time.sleep(1)
									while True:
										try:
											#setRGB(200,20,255)
											#setText("SELEZIONA ORA")
											#time.sleep(1)
											if grovepi.digitalRead(button):
												time.sleep(1)
												sveglia = str("  WAKE UP AT\n    " + whour + ":" + wmin)
												print sveglia
												setRGB(0,255,255)
												setText(" SETTED MINUTE:\n    " + wmin)
												time.sleep(1)
												setText(sveglia)
												time.sleep(1)
												filesveglia = open('/home/pi/sveglia.txt','w')
												filesveglia.write(whour + ":" + wmin)
												filesveglia.close()
												time.sleep(1)
												restart_program()
									######	#restart_program()
											sensor_value = grovepi.analogRead(sensor)
											setRGB(255,0,255)
											minuti = int(sensor_value / 17.1)
											wmin = str("%02d"%minuti)
											setText(wmin)
											time.sleep(.1)
									#			if grovepi.digitalRead(button):
									#				setRGB(0,10,255)
									#				setText("SVEGLIA MIN\n" + whour)
									#				time.sleep(1)
										except IOError:
											print "Error"
								sensor_value = grovepi.analogRead(sensor)
								setRGB(0,0,255)
								ora = int(sensor_value / 44.478)
								whour = str("%02d"%ora)
								setText(whour) 
								time.sleep(.3)

    							except IOError:
        							print "Error"

					if onoff >= "1" and grovepi.digitalRead(button):
						setRGB(100,20,255)
						setText("    WAKE UP AT:\n    " + orasveglia)
						time.sleep(2)
						restart_program()
				except IOError:
                			print "Error"
		time.sleep(1)
		#if val_sveglia == 0 and grovepi.digitalRead(button):
		#	break
		#else:
		#	val_sveglia == 1 and grovepi.digitalRead(button)
		#	print "sveglia on"			
	except (IOError,TypeError) as e:
                print "Error"
                restart_program()

print "ciao"
restart_program()
