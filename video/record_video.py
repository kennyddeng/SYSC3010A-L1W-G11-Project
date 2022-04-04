from pathlib import Path
from picamera import PiCamera
from time import sleep

def record():
    camera = PiCamera()
    camera.start_preview()
    camera.start_recording(str(Path().resolve().parent) + "/SYSC3010A-L1W-G11-Project/recordings/video.h264") # record and save to filename
    print("started video recording")
    sleep(10)
    print("finished video recording")
    camera.stop_recording()
    camera.stop_preview()
    camera.close() # DO NOT DELETE! Need to keep to ensure system/picamera resources
