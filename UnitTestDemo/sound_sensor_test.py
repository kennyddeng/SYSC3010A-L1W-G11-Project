import pyrebase
import RPi.GPIO as GPIO
import time
from datetime import datetime
import unittest

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

# Firebase Database Setup
firebase = pyrebase.initialize_app(config)
db = firebase.database()


# Sound Sensor Setup
channel = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

class TestSoundSensor(unittest.TestCase):
    
    def test_hardware(self):
        stop = False
        def callback(channel):
            if GPIO.input(channel):
                print(GPIO.input(channel))
                self.assertEqual(1, GPIO.input(channel))
            
        GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime = 300)
        GPIO.add_event_callback(channel, callback)
        
        while (stop == False):
            stop = True
            time.sleep(1)
            

        #print("Sound Detected", time.strftime('D%Y-%m-%dT%H:%M:%S'))
        #self.assertEqual(0, gpio)
    
    def test_send_to_firebase(self):
        
        data = {'date':'2022-01-01', 'time':'%00:%00:%00', "value": "Sound Detected"}
      
        #db.child('sensors').child('sound_sensor').child(key).set(data)
        db.child("sensors").child("sound_sensor").child("entries").child('D2022-01-01T00:00:00').set(data)
        #dbEntry = db.child("sensors").child("sound_sensor").child("entries").child('D2022-01-01T00:00:00').get(data)
        dbEntry = db.child("sensors").child("sound_sensor").child("entries").child('D2022-01-01T00:00:00').get().each()
        #print(dbEntry[0].val())
        #print(data["date"])
        
        self.assertEqual(data["date"], dbEntry[0].val()) # test date
        self.assertEqual(data["time"], dbEntry[1].val()) # test time
        self.assertEqual(data["value"], dbEntry[2].val()) # test value
      
if __name__ == "__main__":
    unittest.main()
