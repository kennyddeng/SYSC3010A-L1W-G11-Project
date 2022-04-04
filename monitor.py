import pyrebase
import RPi.GPIO as GPIO
import time
from datetime import datetime
from audio import record_audio, send_audio
from video import record_video, convert_format, send_video

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

def update_video_recordings_db(filename):
    currDateTime = datetime.now()
    date = f"{currDateTime.year:04d}-{currDateTime.month:02d}-{currDateTime.day:02d}"
    curr_time = f"{currDateTime.hour:02d}:{currDateTime.minute:02d}:{currDateTime.second:02d}"
    entry = {"value": filename + ".mp4", "date": date, "time": curr_time}
    db.child("sensors").child("recordings").child("entries").child(time.strftime('D%Y-%m-%dT%H:%M:%S')).set(entry)

def callback(channel):
    if GPIO.input(channel):
        outputEventToConsole()
        writeData()
        record_video.record()  # record_vid
        record_audio.record()  # record_aud
        time.sleep(1)  # add 1 second delay for reliability
        filename = time.strftime('D%Y-%m-%dT%H:%M:%S')
        convert_format.convert_and_merge(filename)  # vid_h264_to_mp4, merge_vid_aud
        time.sleep(1)  # add 1 second delay for reliability
        send_video.send_video_to_firebase_storage(filename)  # upload_vid
        update_video_recordings_db(filename)
        time.sleep(30)
    
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime = 300)
GPIO.add_event_callback(channel, callback)

def loop():
    while True:
        time.sleep(1)
    
if __name__ == "__main__":
    loop()
