import time
import os
from pathlib import Path
from picamera import PiCamera
from time import sleep


def record():
    filename = str(Path().resolve().parent) + "/SYSC3010A-L1W-G11-Project/recordings/video.h264"
    
    # remove existing video file if exists
    if os.path.exists(filename):
      os.remove(filename)

    camera = PiCamera()
    camera.start_preview()
    camera.start_recording(filename)  # record and save to filename
    print("started video recording")
    sleep(9)  # will record for 10 seconds
              # ex. if sleep(10) it records 11 seconds, 1 second extra
    print("finished video recording")
    camera.stop_recording()
    camera.stop_preview()
    camera.close()  # DO NOT DELETE! Need to keep to ensure system/picamera resources
    time.sleep(5)  # add 5 second delay for reliability when saving file (ensure file is saved before file is used)
    