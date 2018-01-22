'''
http://apprize.info/hardware/raspberry/10.html see interrupts.txt

'''
import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

def my_callback(channel):

    print('You pressed the button')

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(16, GPIO.FALLING, callback=my_callback)

i = 0

while True:

    i = i + 1

    print(i)

    time.sleep(1)
