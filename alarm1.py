#!/usr/bin/env python
#
#  alarm_clock_LCD.py
#
# A simple alarm clock using Adafruit_CharLCD module
# plus a buzzer and 16x2 LCD display
#
#
# LCD Screen 16x2 Pins
# --------------------
# Pin 1  to GND
# Pin 2  to 5v
# Pin 3  to variable resistor then to GND 'Contrast Adjustment'
# Pin 4  to GPIO 25 for 'Command or Data Mode Switching'
# Pin 5  to GND for 'Read/Write Mode'
# Pin 6  to GPIO 24 for 'Enable Pin'
# Pin 7  to Not Connected
# Pin 8  to Not Connected
# Pin 9  to Not Connected
# Pin 10 to Not Connected
# Pin 11 to GPIO 23 for 'Data 4'
# Pin 12 to GPIO 17 for 'Data 5'
# Pin 13 to GPIO 21 for 'Data 6'
# Pin 14 to GPIO 22 for 'Data 7'
# Pin 15 to 5v for 'Backlight Anode' - Could use variable resistor as a 'Brightness Control'
# Pin 16 to GND for 'LED Backlight Cathode'
#
# The positive side of the two pin active buzzer is attached to pin 18
# and the other pin goes to ground
#
#  Copyright 2015  Ken Powers
# 
 
# Import the required libraries
from Adafruit_CharLCD import Adafruit_CharLCD
import time
import RPi.GPIO as GPIO
 
# Set GPIO pins to Broadcom numbering system
GPIO.setmode(GPIO.BCM)
 
# Set some global constants
lcd = Adafruit_CharLCD()
buzzer_pin = 18
RUNNING = True
 
# Set buzzer pin as a GPIO output
GPIO.setup(buzzer_pin, GPIO.OUT)
 
# Make the function to create a buzzing sound
# This function was originally written by Simon Monk
def buzz(pitch, duration):
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duration * pitch)
    for i in range(cycles):
        GPIO.output(buzzer_pin, True)
        time.sleep(delay)
        GPIO.output(buzzer_pin, False)
        time.sleep(delay)
 
try:
    # Get alarm time from user
    response = raw_input("Enter the alarm time in 24-Hour format HHMM: ")
    print("Alarm time has been set for %s hrs" % response)
    buzz(500,0.1)
 
    alarm = int(response)
 
    # Clear LCD screen
    lcd.clear()
 
    while RUNNING:
        # Continually get the time as an integer
        # Output time in 24-Hour format to the LCD
        curr_time = int(time.strftime("%H%M"))
        lcd.home()
        lcd.message("  Current Time\n")
        lcd.message(time.strftime("    %H:%M:%S\n"))
 
        # Trigger the buzzer function when the alarm time is reached
        # The buzzer will have two different tones just for fun
        if curr_time == alarm:
            lcd.clear()
            lcd.home()
            lcd.message("    Wake Up!")
            buzz(10,0.5)
            time.sleep(0.25)
            buzz(20,0.5)
            time.sleep(0.25)
 
except KeyboardInterrupt:
    RUNNING = False
    print "\nQuitting"
 
# Clear LCD screen upon exit
# Don't forget to clean up after so we
# can use the GPIO next time
finally:
    lcd.clear()
    GPIO.cleanup()