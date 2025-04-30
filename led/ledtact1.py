import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


LED = 11
LED1 = 13
LED2 = 15
Switch = 10

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

flag = False

while True:
	if GPIO.input(Switch) == GPIO.HIGH:
		print("Button was pushed!")
		GPIO.output(LED, flag)
		GPIO.output(LED1, flag)
		GPIO.output(LED2, flag)
		flag = not flag
		time.sleep(1)
