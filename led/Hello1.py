import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

LED = 11
LED1 = 13
LED2 = 15

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)git a
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)
try:
	while True:
		key = int(input("press key"))
		if key == 1:
			GPIO.output(LED, GPIO.HIGH)
			GPIO.output(LED1, GPIO.HIGH)
			GPIO.output(LED2, GPIO.HIGH)
		elif key == 0:
			GPIO.output(LED, GPIO.LOW)
			GPIO.output(LED1, GPIO.LOW)
			GPIO.output(LED2, GPIO.LOW)
finally:
	GPIO.cleanup()
			
				

