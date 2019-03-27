
import RPi.GPIO as GPIO
from picamera import PiCamera
import time

# sensor set up
channel = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# camera set up
camera = PiCamera()
camera.rotation = 180

# not sure if this is a good idea or not...
picCount = 0

# what to do when sensor gets input
def callback(channel):
        global picCount
        if GPIO.input(channel):
                camera.capture('/home/pi/BirdStrikePi/pictures/birdPic%s.jpg' % picCount)
                picCount += 1
        else:
                camera.capture('/home/pi/BirdStrikePi/pictures/birdPic%s.jpg' % picCount)
                picCount += 1

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  
GPIO.add_event_callback(channel, callback)  

# keep the code running
while True:
        time.sleep(1)
