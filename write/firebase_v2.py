from firebase import Firebase
from sense_hat import SenseHat
import time
from datetime import datetime
from notify import Notify

sense = SenseHat()
temp = sense.get_temperature()
max_temperature = 0
min_temperature = 0
notify = Notify()


def write_to_db(db) -> None:

    '''
    This function writes to the firebase database.
    Collects sensehat data (temperature) and pushes it as an entry.
    '''

    sense = SenseHat()

    while True:
        currDateTime = datetime.now()

        date = f"{currDateTime.year:04d}-{currDateTime.month:02d}-{currDateTime.day:02d}"
        currTime = f"{currDateTime.hour:02d}:{currDateTime.minute:02d}:{currDateTime.second:02d}"

        entry = {"value": sense.get_temperature(), "date": date, "time": currTime}
        db.child("sensors").child(123).child("entries").push(entry)
        time.sleep(3)


def stream_handler(message) -> None:

    '''
    This function checks the database constantly for any changes made to the set threshold values.
    If there is a change detected the user will receive an SMS notification.
    '''

    print(message)
    curr_temp = temp

    if list(message['data'])[0] == "max_temperature":

        max_temperature = message['data']['max_temperature']
        if curr_temp > max_temperature:
            msg = "temperature above threshold"
            notify.notify_users(msg=msg, users=3)
            time.sleep(20)

    elif list(message['data'])[0] == "min_temperature":

        min_temperature = message['data']['min_temperature']
        if curr_temp < min_temperature:
            msg = "temperature below threshold"
            notify.notify_users(msg=msg, users=3)
            time.sleep(20)


my_stream = Firebase().db.child('sensors').child('123').stream(stream_handler)


def main():
    write_to_db(db=Firebase().db)


if __name__ == "__main__":
    main()


'''
flake8 output:

firebase_v2.py:26:80: E501 line too long (89 > 79 characters)
#format of the date being pushed to database.

firebase_v2.py:27:80: E501 line too long (97 > 79 characters)
#format of the time being pushed to database.

firebase_v2.py:29:80: E501 line too long (82 > 79 characters)
#format of the time being pushed to database.

firebase_v2.py:37:80: E501 line too long (98 > 79 characters)
#Commentation
'''
