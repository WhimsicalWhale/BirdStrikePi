
import RPi.GPIO as GPIO
from picamera import PiCamera
import time
import os

# sensor set up
channel = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# camera set up
camera = PiCamera()
camera.rotation = 180
camera.framerate = 90
camera.resolution = '1280x720'
camera.shutter_speed = 800


home = os.getcwd()

# what to do when sensor gets input
def callback(channel):
        if GPIO.input(channel):
            for i, filename in enumerate(camera.capture_continuous('%s/pictures/img{counter:03d}.jpg' % home)):
                if i == 15:
                    break
        else:
            for i, filename in enumerate(camera.capture_continuous('%s/pictures/img{counter:03d}.jpg' % home)):
                if i == 15:
                    break

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  
GPIO.add_event_callback(channel, callback)  

# keep the code running
while True:
        time.sleep(.1)
