import pyrebase
from sense_hat import SenseHat
import time
from datetime import datetime
from notify import *
from twilio.rest import Client ## pip install twilio

config = {
  "apiKey": "AIzaSyBWMHPeUjEqT_P6g_jrxlKC431pr2xkTaU",
  "authDomain": "sysc3010-project.firebaseapp.com",
  "databaseURL": "https://sysc3010-project-default-rtdb.firebaseio.com/",
  "storageBucket": "sysc3010-project.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
sense = SenseHat()
temp = sense.get_temperature()

def write_to_db():
   
    sense = SenseHat()

    while True:
        currDateTime = datetime.now()

        date = f"{currDateTime.year:04d}-{currDateTime.month:02d}-{currDateTime.day:02d}"
        currTime = f"{currDateTime.hour:02d}:{currDateTime.minute:02d}:{currDateTime.second:02d}"

        data = {"type": "temperature", "max_temperature": 38, "min_temperature": 35}
        entry = {"value": sense.get_temperature(), "date": date, "time": currTime, "threshold": data}
        db.child("sensors").child(123).child("entries").set(entry)
        time.sleep(3)
       
def stream_handler(message):
    
    curr_temp = temp
    
    if message['path'] == '/max_temperature':
        if curr_temp > message['data']:
            msg = "temperature above threshold"   
                
    elif message['path'] == '/min_temperature':
        if curr_temp < message['data']:
            msg = "temperature below threshold"
            
            
                   
my_stream = db.child('sensors').child('123').child('entries').child('threshold').stream(stream_handler)

if __name__ == "__main__":
    write_to_db()
    notify = Notify()
    user = 3
    notify.notify_users(msg=msg, users=user)
