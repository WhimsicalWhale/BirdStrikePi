from picamera import PiCamera # for the camera
import time # for timing purposes
import os # for deleting files

# create the class to interact with the camera
camera = PiCamera()

# so the picture isn't uspide down the way I have it set up
camera.rotation = 180

# messing around with other settings
camera.framerate = 90

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

# doing some work testing the capture_continuous method
camera.start_preview()
start = time.time()

for filename in camera.capture_continuous('/home/pi/BirdStrikePi/pictures/img{counter:03d}.jpg'):
     print('%s' % filename, time.time() - start)     
     
camera.stop_preview()
'''

# this section of code will continously take photos, deleting older ones as new ones are taken
camera.start_preview()
start = time.time()

try:
    for i, filename in enumerate(camera.capture_continuous('%s/pictures/img{counter:03d}.jpg' % os.getcwd())):
        print(filename, time.time() - start)
        
        if i > 15:
            os.remove(os.getcwd() + '/pictures/img%03d.jpg' % (i-15))
        
finally:
    camera.stop_preview()
