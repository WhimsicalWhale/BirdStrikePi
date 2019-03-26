
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

# what to do when sensor gets input
def callback(channel):
        if GPIO.input(channel):
                print("Collision Detected!")
                camera.capture('/home/pi/BirdStrikePi/pictures/theif.jpg')
        else:
                print("Collision Detected!")
                camera.capture('/home/pi/BirdStrikePi/pictures/theelse.jpg')

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  
GPIO.add_event_callback(channel, callback)  

# keep the code running
while True:
        time.sleep(1)
