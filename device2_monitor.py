import time
import RPi.GPIO as GPIO
from datetime import datetime
from multiprocessing import Process
from audio import record_audio
from video import record_video, convert_format, send_video
from Python_Modules.firebase import Firebase
from Python_Modules.notify import Notify


# Firebase Database Setup
firebase = Firebase()
db = firebase.db

# Twilio Setup
notify = Notify()

# Sound Sensor Setup
channel = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

key = 0
wait_interval = 60  # minimum number of seconds between possible recordings


def writeData():
    data = {'date': time.strftime('%Y-%m-%d'),
            'time': time.strftime('%H:%M:%S'),
            "value": "Sound Detected"}

    global key
    db.child("sensors").child("sound_sensor").child("entries").child(time.strftime('D%Y-%m-%dT%H:%M:%S')).set(data)
    key += 1


def notify_user(time):
    notify.notify_users(msg = "Sound Detected at " + time)


def outputEventToConsole(event):
    print(time.strftime('D%Y-%m-%dT%H:%M:%S'), event)


def rec_vid():
    record_video.record()


def rec_aud():
    record_audio.record()


def update_video_recordings_db(filename):
    currDateTime = datetime.now()
    date = f"{currDateTime.year:04d}-{currDateTime.month:02d}-{currDateTime.day:02d}"
    curr_time = f"{currDateTime.hour:02d}:{currDateTime.minute:02d}:{currDateTime.second:02d}"
    entry = {"value": filename + ".mp4", "date": date, "time": curr_time}
    db.child("sensors").child("recordings").child("entries").child(time.strftime('D%Y-%m-%dT%H:%M:%S')).set(entry)


def callback(channel):
    if GPIO.input(channel):
        outputEventToConsole("Sound Detected")
        filename = time.strftime('D%Y-%m-%dT%H:%M:%S')
        writeData()
        notify_user(filename)

        # record video and audio concurrently
        p1 = Process(target=rec_vid)
        p1.start()
        p2 = Process(target=rec_aud)
        p2.start()
        p1.join()
        p2.join()

        convert_format.convert_and_merge(filename)  # vid_h264_to_mp4, merge_vid_aud
        send_video.send_video_to_firebase_storage(filename)  # upload_vid
        update_video_recordings_db(filename)
        outputEventToConsole("Firebase recordings database updated")
        time.sleep(wait_interval)


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)


def loop():
    while True:
        time.sleep(1)


if __name__ == "__main__":
    loop()
