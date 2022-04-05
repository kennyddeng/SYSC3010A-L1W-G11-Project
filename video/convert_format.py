import os
import time
import moviepy.editor as mpe
from subprocess import call
from pathlib import Path


def h264_to_mp4(filename):
    nameOld = str(Path().resolve().parent) + "/SYSC3010A-L1W-G11-Project/recordings/" + filename + ".h264"
    nameNew = str(Path().resolve().parent) + "/SYSC3010A-L1W-G11-Project/recordings/" + filename + ".mp4"
     
    # remove existing video file if exists
    if os.path.exists(nameNew):
      os.remove(nameNew)
      
    call(["MP4Box", "-add", nameOld, nameNew])
    time.sleep(5)  # add 5 second delay for reliability when saving file (ensure file is saved before file is used)
    
    
def merge_wav_mp4(vidName, audName, outName):
    # remove existing video file if exists
    if os.path.exists(outName):
      os.remove(outName)
      
    call(["ffmpeg", "-i", vidName, "-i", audName, "-c:v", "copy", "-c:a", "aac", "-map", "0:v:0", "-map", "1:a:0", outName])    
    time.sleep(5)  # add 5 second delay for reliability when saving file (ensure file is saved before file is used)
    
    
def convert_and_merge(filename):
    h264_to_mp4("video")
    vidName = str(Path().resolve().parent) + "/SYSC3010A-L1W-G11-Project/recordings/" + "video" + ".mp4"
    audName = str(Path().resolve().parent) + "/SYSC3010A-L1W-G11-Project/recordings/" + "audio" + ".wav"
    outName = str(Path().resolve().parent) + "/SYSC3010A-L1W-G11-Project/recordings/" + filename + ".mp4"
    merge_wav_mp4(vidName, audName, outName)
