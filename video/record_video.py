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
    # will record for 10 seconds
    # ex. if sleep(10) it records 11 seconds, 1 second extra
    sleep(9)
    print("finished video recording")
    camera.stop_recording()
    camera.stop_preview()
    # DO NOT DELETE! Need to keep to ensure system/picamera resources
    camera.close()
    # add 5 second delay for reliability when saving file
    # (ensure file is saved before file is used)
    time.sleep(5)
