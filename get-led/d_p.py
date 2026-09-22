import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [16,12,25,17,27,23,22,24] 
GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

up = 9
dn = 10
GPIO.setup(up, GPIO.IN)
GPIO.setup(dn, GPIO.IN)

num = 0

def d2b(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

while True:
    if GPIO.input(up) and GPIO.input(dn):
        while True:
            GPIO.output(leds, 255)
            num = 255
            
    elif GPIO.input(up):
        num += 1
        print(num,d2b(num))
        if num < 0:
            num = 0
        elif num > 255:
            num = 0
        time.sleep(sleep_time)
    elif GPIO.input(dn):
        num -= 1
        print(num,d2b(num))
        if num < 0:
            num = 0
        elif num > 256:
            num = 0
        time.sleep(sleep_time)
    GPIO.output(leds, d2b(num))