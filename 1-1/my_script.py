import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.OUT)


val = GPIO.input(20)
GPIO.output(21, val)


