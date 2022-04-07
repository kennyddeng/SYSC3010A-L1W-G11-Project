import sys
from pathlib import Path
sys.path.append("..")  # must go before Python_Modules.firebase import
from Python_Modules.firebase import Firebase


# Firebase Storage Setup
firebase = Firebase()
sr = firebase.sr


def send_video_to_firebase_storage(filename):
    name = str(Path().resolve()) + "/recordings/" + filename + ".mp4"
    sr.child("recordings").child("video").child(filename + ".mp4").put(name)
    print(name, "sent to Firebase Storage")
