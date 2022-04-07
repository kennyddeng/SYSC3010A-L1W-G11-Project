import os
import time
from subprocess import call
from pathlib import Path


def h264_to_mp4(filename):
    name_old = str(Path().resolve().parent) + "/SYSC3010A-L1W-G11-Project/recordings/" + filename + ".h264"
    name_new = str(Path().resolve().parent) + "/SYSC3010A-L1W-G11-Project/recordings/" + filename + ".mp4"

    # remove existing video file if exists
    if os.path.exists(name_new):
        os.remove(name_new)

    call(["MP4Box", "-add", name_old, name_new])
    # add 5 second delay for reliability when saving file
    # (ensure file is saved before file is used)
    time.sleep(5)


def merge_wav_mp4(vid_name, aud_name, out_name):
    # remove existing video file if exists
    if os.path.exists(out_name):
        os.remove(out_name)

    call(["ffmpeg", "-i", vid_name, "-i", aud_name, "-c:v", "copy", "-c:a", "aac", "-map", "0:v:0", "-map", "1:a:0", out_name])
    # add 5 second delay for reliability when saving file
    # (ensure file is saved before file is used)
    time.sleep(5)


def convert_and_merge(filename):
    h264_to_mp4("video")
    vid_name = str(Path().resolve().parent) + "/SYSC3010A-L1W-G11-Project/recordings/" + "video" + ".mp4"
    aud_name = str(Path().resolve().parent) + "/SYSC3010A-L1W-G11-Project/recordings/" + "audio" + ".wav"
    out_name = str(Path().resolve().parent) + "/SYSC3010A-L1W-G11-Project/recordings/" + filename + ".mp4"
    merge_wav_mp4(vid_name, aud_name, out_name)
