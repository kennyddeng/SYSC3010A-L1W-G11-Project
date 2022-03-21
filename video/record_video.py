from pathlib import Path
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
camera.start_recording(str(Path().resolve().parent) + "/recordings/video0.h264") # record and save to filename
print("started recording")
sleep(5)
print("finished recording")
camera.stop_recording()
camera.stop_preview()
camera.close() # DO NOT DELETE! Need to keep to ensure system/picamera resources