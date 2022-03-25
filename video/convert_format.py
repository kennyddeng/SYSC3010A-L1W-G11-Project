from subprocess import call
from pathlib import Path
import moviepy.editor as mpe

def h264_to_mp4(filename):
    #cmd = "MP4Box -add video0.h264 video0.mp4"
    nameOld = str(Path().resolve().parent) + "/recordings/" + filename + ".h264"
    nameNew = str(Path().resolve().parent) + "/recordings/" + filename + ".mp4"
    #cmd = "MP4Box -add nameOld nameNew"
    #call([cmd], shell=True)
    call(["MP4Box", "-add", nameOld, nameNew])

def merge_wav_mp4(vidName, audName, outName):
    #call(["ffmpeg", "-i", vidName, "-i", audName, "-c", "copy", outName])
    call(["ffmpeg", "-i", vidName, "-i", audName, "-c:v", "copy", "-c:a", "aac", "-map", "0:v:0", "-map", "1:a:0", outName])    

if __name__ == "__main__":
    h264_to_mp4("video0")
    vidName = str(Path().resolve().parent) + "/recordings/" + "video0" + ".mp4"
    audName = str(Path().resolve().parent) + "/recordings/" + "test0" + ".wav"
    outName = str(Path().resolve().parent) + "/recordings/" + "stimk" + ".mp4"
    merge_wav_mp4(vidName, audName, outName)