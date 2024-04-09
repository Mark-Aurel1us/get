import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

dig = 8
U0 = 3.3
dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13
for a in dac:
	GPIO.setup(a,GPIO.OUT)
GPIO.setup(comp,GPIO.IN)
GPIO.setup(troyka,GPIO.OUT)
GPIO.output(troyka, 1)


def dec2bin(x):
	a = []
	for i in range(dig):
		a = [x%2]+a
		x=x//2
	return a

def bin2dec(x):
	y = 0
	for i in range(dig):
		y = y + x[-1-i]*2**i
	return y
		

def setpins(bins):
	for i in range(dig):
		GPIO.output(dac[i], bins[i])

def adc1():
	for x in range(2**dig):
		setpins(dec2bin(x))
		time.sleep(0.001)
		if GPIO.input(comp):
			return x
	return 256
	
def adc():
	x = dec2bin(0)
	for i in range(dig):
		x[i]=1
		setpins(x)
		time.sleep(0.01)
		if GPIO.input(comp):
			x[i]=0


	return bin2dec(x)+1

try:
	while True:
		x = adc()
		time.sleep(0.01)
		print(x,"  ",x/(2**dig)*U0)
except KeyboardInterrupt:
	print("program interrupted")
