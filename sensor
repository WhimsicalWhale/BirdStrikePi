
import RPi.GPIO as GPIO
import time

channel = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
        if GPIO.input(channel):
                print("Collision Detected!")
        else:
                print("Collision Detected!")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  
GPIO.add_event_callback(channel, callback)  

while True:
        time.sleep(1)
