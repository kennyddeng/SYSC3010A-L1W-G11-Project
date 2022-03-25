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
max_temperature = 0
min_temperature = 0
notify = Notify()

def write_to_db():
   
    sense = SenseHat()

    while True:
        currDateTime = datetime.now()

        date = f"{currDateTime.year:04d}-{currDateTime.month:02d}-{currDateTime.day:02d}"
        currTime = f"{currDateTime.hour:02d}:{currDateTime.minute:02d}:{currDateTime.second:02d}"
        
        entry = {"value": sense.get_temperature(), "date": date, "time": currTime}
        db.child("sensors").child(123).child("entries").set(entry)
        time.sleep(3)
       

def read_from_db(db):
    entries = db.child("sensors").child(123).child("entries").get().each()
    for entry in entries:
        value = entry.val()["value"]
        date = entry.val()["date"]
        time = entry.val()["time"]
        print("Values: {}, Date: {}, Time: {}".format(value, date, time))

def stream_handler(message):
    
    curr_temp = temp
    
    if message['path'] == '/max_temperature':
        max_temperature = message['data']
        if curr_temp > max_temperature:
            msg = "temperature above threshold"
            user = 3
            notify.notify_users(msg=msg, users=user)
            
                
    elif message['path'] == '/min_temperature':
        min_temperature = message['data']
        if curr_temp < min_temperature:
            msg = "temperature below threshold"
            user = 3
            notify.notify_users(msg=msg, users=user)
                                         
my_stream = db.child('sensors').child('123').child('entries').stream(stream_handler)


def main():
    write_to_db()
    
    
if __name__ == "__main__":
    main()
