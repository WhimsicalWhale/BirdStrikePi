
import RPi.GPIO as GPIO
import picamera
import io # I think I need this for the camera loop?


# sensor set up
channel = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# camera set up
camera = picamera.PiCamera()
camera.rotation = 180
'''
camera.framerate = 90
camera.resolution = '1280x720'
camera.shutter_speed = 800
'''

# set up a stream?
stream = picamera.PiCameraCircularIO(camera, seconds = 6)
camera.start_recording(stream, format='h264')


'''
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
'''

count = 0

# keep the code running
try:
    while True:
        camera.wait_recording(1)
        if GPIO.input(channel):
            print("motion detected")
            camera.wait_recording(3)
            stream.copy_to('motion%s.h264' % count)
            count += 1
        else:
            print("motion detected")
            camera.wait_recording(3)
            stream.copy_to('motion%s.h264' % count)
            count += 1
            
finally:
    camera.stop_recording()