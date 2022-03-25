import pyrebase
import RPi.GPIO as GPIO
import time
from datetime import datetime

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

key = 0

def writeData():
    data = {'date':time.strftime('%Y-%m-%d'), 'time':time.strftime('%H:%M:%S'), "value": "Sound Detected"}
    
    global key    
    #db.child('sensors').child('sound_sensor').child(key).set(data)
    db.child("sensors").child("sound_sensor").child("entries").child(time.strftime('D%Y-%m-%dT%H:%M:%S')).set(data)
    key += 1
    
def outputEventToConsole():
    print("Sound Detected", time.strftime('D%Y-%m-%dT%H:%M:%S'))

def callback(channel):
    if GPIO.input(channel):
        outputEventToConsole()
        writeData()
        #time.sleep(10)
    
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime = 300) # bouncetime is # ms between samples
GPIO.add_event_callback(channel, callback)

def loop():
    while True:
        time.sleep(1)
    
if __name__ == "__main__":
    loop()