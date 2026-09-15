import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
d_l = 6
GPIO.setup(d_l, GPIO.IN)

state = 0
while True:
    if not GPIO.input(d_l):
        state = not state
        GPIO.output(led, state)
