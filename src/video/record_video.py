from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.start_recording("video2.h264")
print("started recording")
sleep(5)
print("finished recording")
camera.stop_recording()
camera.stop_preview()
camera.close() # DO NOT DELETE! Need to keep to ensure system/picamera resources