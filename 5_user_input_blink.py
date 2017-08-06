#!/usr/bin/python

import os
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

#Setup variables for user input
led_choice = 0
count = 0

os.system('clear')

print "Which LED would you like to blink"
print "1: Red?"
print "2: Blue?"

led_choice = input("Choose your option: ") # ask for an input

if led_choice == 1:
    os.system('clear')
    print "You picked the Red LED"
    count = input("How many times would you like it to blink?: ")
    while count > 0: # while the value of count is greater than 0
        GPIO.output(27,GPIO.HIGH)
        sleep(1)
        GPIO.output(27,GPIO.LOW)
        sleep(1)
        count = count - 1 # reduce the value of count by 1

if led_choice == 2:
    os.system('clear')
    print "You picked the Red LED"
    count = input("How many times would you like it to blink?: ")
    while count > 0: # while the value of count is greater than 0
        GPIO.output(17,GPIO.HIGH)
        sleep(1)
        GPIO.output(17,GPIO.LOW)
        sleep(1)
        count = count - 1 # reduce the value of count by 1