import RPi.GPIO as GPIO
import time
dac = 8
number = [0,0,0,0,0,0,0,0]
leds2 = [8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)

for i in range(dac):
	GPIO.setup(leds2[i],GPIO.OUT)

for a in range(20):
	b = int(input())
	for i in range(dac):
		number[dac - i - 1] = b%2
		b = b // 2
		GPIO.output(leds2[dac - i - 1], number[dac-i-1])
	# time.sleep(20)
	
GPIO.cleanup()
