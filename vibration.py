from gpiozero import MotionSensor

pir = MotionSensor(4)
pir.wait_for_motion()
print("Motion detected!")

'''
Code copied from piddlerintheroot, doesn't seem to work

import RPi.GPIO
import time

#GPIO setup
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
	if GPIO.input(channel):
		print("Movement detected!")
	else:
		print("Movement detected!")

# let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# assign function to GPIO PIN, run function on change
GPIO.add_event_callback(channel, callback)

# infinite loop to keep program running
while True:
	time.sleep(1)
'''
