from pathlib import Path
import sys
sys.path.append("..")
from Python_Modules.firebase import Firebase


# Firebase Storage Setup
firebase = Firebase()
sr = firebase.sr


def send_video_to_firebase_storage(filename):
    name = str(Path().resolve()) + "/recordings/" + filename + ".mp4"
    sr.child("recordings").child("video").child(filename + ".mp4").put(name)
    print(name, "sent to Firebase Storage")
    