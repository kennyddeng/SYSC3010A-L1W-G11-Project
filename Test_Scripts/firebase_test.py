from firebase import * # The firebase.py file needs to be in the same directory as this file in order to use it
from sense_hat import SenseHat
import time
from datetime import datetime

def write_to_db(db):
    sense = SenseHat()

    currDateTime = datetime.now()

    date = f"{currDateTime.year:04d}-{currDateTime.month:02d}-{currDateTime.day:02d}"
    time = f"{currDateTime.hour:02d}:{currDateTime.minute:02d}:{currDateTime.second:02d}"

    data = {"type": "temperature", "min_temperature": 18.0, "max_temperature": 25.0}
    entry = {"value": sense.get_temperature(), "date": date, "time": time}
    db.child("sensors").child(123).child("entries").push(entry)

def read_from_db(db):
    entries = db.child("sensors").child(123).child("entries").get().each()
    for entry in entries:
        value = entry.val()["value"]
        date = entry.val()["date"]
        time = entry.val()["time"]
        print("Values: {}, Date: {}, Time: {}".format(value, date, time))

if __name__ == "__main__":
    write_to_db(db=Firebase().db)
    read_from_db(db=Firebase().db)