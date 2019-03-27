from picamera import PiCamera
import time

# create the class to interact with the camera
camera = PiCamera()

# so the picture isn't uspide down the way I have it set up
camera.rotation = 180

# messing around with other settings
camera.framerate = 60

'''
# see what the camera sees for 3 secs
camera.start_preview()
time.sleep(5)
camera.stop_preview()

# take 5 pictures in a row
camera.start_preview()
for i in range(5):
    camera.capture('/home/pi/BirdStrikePi/pictures/image%s.jpg' % i)
camera.stop_preview()
'''

# doing some work testing the capture_continuous method
camera.start_preview()
start = time.time()

for filename in camera.capture_continuous('/home/pi/BirdStrikePi/pictures/img{counter:03d}.jpg'):
     print('%s' % filename, time.time() - start)
     
camera.stop_preview()
