from picamera import PiCamera
from time import sleep

# create the class to interact with the camera
camera = PiCamera()

# so the picture isn't uspide down the way I have it set up
camera.rotation = 180

# see what the camera sees for 3 secs
camera.start_preview()
sleep(5)
camera.stop_preview()

# take 5 pictures in a row
camera.start_preview()
for i in range(5):
	camera.capture('/home/pi/BirdStrike/pictures/image%s.jpg' % i)
camera.stop_preview()
