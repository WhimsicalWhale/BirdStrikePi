
import RPi.GPIO as GPIO
import picamera
import io # I think I need this for the camera loop?
import datetime

# sensor set up
channel = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# camera set up
camera = picamera.PiCamera()
camera.rotation = 180
camera.framerate = 75
camera.resolution = '640x480'


# set up a stream?
stream = picamera.PiCameraCircularIO(camera, seconds = 6)
camera.start_recording(stream, format='h264')


'''
# takes pictures when sensor reads input, too slow
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
'''


# keep the code running
try:
    while True:
        camera.wait_recording(1)
        if GPIO.input(channel):
            camera.wait_recording(3)
            stream.copy_to('%s.h264' % datetime.datetime.now())
        else:
            camera.wait_recording(3)
            stream.copy_to('%s.h264' % datetime.datetime.now())
finally:
    camera.stop_recording()
