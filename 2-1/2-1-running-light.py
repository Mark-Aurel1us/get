import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [2,3,4,17,27,22,10,9]

for i in leds:
	GPIO.setup(i,GPIO.OUT)
for a in range(100):
	for i in leds:
		GPIO.output(i,1)
		time.sleep(0.1)
		GPIO.output(i,0)

GPIO.cleanup()


