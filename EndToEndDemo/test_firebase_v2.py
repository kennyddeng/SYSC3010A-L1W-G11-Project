import pyrebase
from sense_hat import SenseHat
import time
from datetime import datetime

config = {
  "apiKey": "AIzaSyBwivJ2TwbSkOEucx481IcMrZ8PIoY56Gc",
  "authDomain": "fir-test-project-6c2f9.firebaseapp.com",
  "databaseURL": "https://fir-test-project-6c2f9-default-rtdb.firebaseio.com/",
  "storageBucket": "fir-test-project-6c2f9.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
sense = SenseHat()
temp = sense.get_temperature()

def write_to_db():
   
    while True:   
       data = {'date':time.strftime('%Y-%m-%d'),
               'time':time.strftime('%H:%M:%S'),
               'max_temperature': 38,
               'min_temperature': 35,
               'threshold': {'max_temperature': 38,'min_temperature': 35, 'temperature':sense.get_temperature()},
               'temperature':sense.get_temperature()}
       temp = sense.get_temperature()

       db.child('sensors').child('current').set(data)
        
       time.sleep(3)
       
if __name__ == "__main__":
    write_to_db()