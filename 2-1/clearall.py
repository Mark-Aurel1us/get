import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

clear= [2,3,4,17,27,22,10,9,8,11,7,1,0,5,12,6]

for i in clear:
	GPIO.setup(i,GPIO.OUT)
for i in clear:
	GPIO.output(i,0)

GPIO.cleanup()


