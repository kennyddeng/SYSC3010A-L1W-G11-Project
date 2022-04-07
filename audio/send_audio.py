from pathlib import Path
import sys
sys.path.append("..")  # must go before Python_Modules.firebase import
from Python_Modules.firebase import Firebase


# Firebase Storage Setup
firebase = Firebase()
sr = firebase.sr


def send_audio_to_firebase_storage():
    name = str(Path().resolve()) + "/recordings/audio.wav"
    sr.child("recordings").child("audio").child("audio.wav").put(name)
    print(name, "sent to Firebase Storage")


if __name__ == "__main__":
    send_audio_to_firebase_storage()
