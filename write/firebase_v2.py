from firebase import *
import pyrebase
from sense_hat import SenseHat
import time
from datetime import datetime
from notify import *
from twilio.rest import Client ## pip install twilio


sense = SenseHat()
temp = sense.get_temperature()
max_temperature = 0
min_temperature = 0
notify = Notify()

def write_to_db(db):
   
    sense = SenseHat()

    while True:
        currDateTime = datetime.now()

        date = f"{currDateTime.year:04d}-{currDateTime.month:02d}-{currDateTime.day:02d}"
        currTime = f"{currDateTime.hour:02d}:{currDateTime.minute:02d}:{currDateTime.second:02d}"
        
        entry = {"value": sense.get_temperature(), "date": date, "time": currTime}
        db.child("sensors").child(123).child("entries").set(entry)
        time.sleep(3)
       

def stream_handler(message):
    print(message)
    curr_temp = temp
    
    if message['path'] == '/max_temperature':
        max_temperature = message['data']
        if curr_temp > max_temperature:
            msg = "temperature above threshold"
            notify.notify_users(msg=msg)
            time.sleep(20)        
                
    elif message['path'] == '/min_temperature':
        min_temperature = message['data']
        if curr_temp < min_temperature:
            msg = "temperature below threshold"
            notify.notify_users(msg=msg)
            time.sleep(20)
                                        
my_stream = Firebase().db.child('sensors').child('123').stream(stream_handler)

def main():
    write_to_db(db=Firebase().db)
    
 
if __name__ == "__main__":
    main()
