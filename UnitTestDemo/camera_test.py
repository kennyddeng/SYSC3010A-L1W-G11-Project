from pathlib import Path
from picamera import PiCamera
from time import sleep
import pyrebase
import unittest

class TestCamera(unittest.TestCase):
    def test_hardware(self):
        fileExists = False # boolean if saved video file exists
        filename = str(Path().resolve().parent) + "/recordings/test0.h264"
        camera = PiCamera()
        camera.start_preview()
        camera.start_recording(filename) # record and save to filename
        print("started recording")
        sleep(5)
        print("finished recording")
        camera.stop_recording()
        camera.stop_preview()
        camera.close() # DO NOT DELETE! Need to keep to ensure system/picamera resources

        if Path(filename).is_file():
            # file exists
            exists = True
        
        self.assertEqual(True, exists)
    def test_send_to_firebase(self):
        # Firebase Config
        api_key = "AIzaSyBWMHPeUjEqT_P6g_jrxlKC431pr2xkTaU"
        project_id = "sysc3010-project"
        database_url = "https://sysc3010-project-default-rtdb.firebaseio.com/"

        config = {
        "apiKey": api_key,
        "authDomain": "{}.firebaseapp.com".format(project_id),
        "databaseURL": database_url,
        "storageBucket": "{}.appspot.com".format(project_id)
        }

        # Firebase Storage Setup
        firebase = pyrebase.initialize_app(config)
        sr = firebase.storage()

        name = str(Path().resolve().parent) + "/recordings/test0.h264"
        sr.child("recordings").child("video").child("test0.h264").put(name)
        print(name, "sent to Firebase Storage")
        
        dbEntryURL = sr.child("recordings").child("video").child("test0.h264").get_url(None)
        vidFilePathURL = "https://firebasestorage.googleapis.com/v0/b/sysc3010-project.appspot.com/o/recordings%2Fvideo%2Ftest0.h264?alt=media"
        #print(storage.child().get_url(None))
        #print(dbEntryURL)
        self.assertEqual(dbEntryURL, vidFilePathURL)  

if __name__ == "__main__":
    unittest.main()
