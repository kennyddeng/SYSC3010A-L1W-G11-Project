from firebase import Firebase
from sense_emu import SenseHat
import time
from datetime import datetime
from notify import Notify

sense = SenseHat()
max_temperature = 0
min_temperature = 0
notify = Notify()


def write_to_db(db) -> None:

    '''
    This function writes to the firebase database.
    Collects sensehat data (temperature) and pushes it as an entry.
    '''

    sense = SenseHat()

    global max_temperature

    max_temperature = db.child("sensors").child(123).get().val()['max_temperature']

    global min_temperature

    min_temperature = db.child("sensors").child(123).get().val()['min_temperature']

    while True:

        current_temp = sense.get_temperature()

        currDateTime = datetime.now()

        date = f"{currDateTime.year:04d}-{currDateTime.month:02d}-{currDateTime.day:02d}"

        currTime = f"{currDateTime.hour:02d}:{currDateTime.minute:02d}:{currDateTime.second:02d}"

        entry = {"value": current_temp, "date": date, "time": currTime}

        db.child("sensors").child(123).child("entries").push(entry)

        time.sleep(3)

        print(current_temp)
    
        if current_temp > max_temperature:
            msg = "temperature above threshold"
            notify.notify_users(msg=msg, users=3)
            time.sleep(10)

        elif current_temp < min_temperature:
            msg = "temperature below threshold"
            notify.notify_users(msg=msg, users=3)
            time.sleep(10)


def stream_handler(message) -> None:

    '''
    This function checks the database constantly for any changes made to the set threshold values.
    If there is a change detected the user will receive an SMS notification.
    '''

    global max_temperature

    global min_temperature

    if list(message['data'])[0] == "max_temperature":

        max_temperature = message['data']['max_temperature']

    elif list(message['data'])[0] == "min_temperature":

        min_temperature = message['data']['min_temperature']


my_stream = Firebase().db.child('sensors').child('123').stream(stream_handler)


def main():
    write_to_db(db=Firebase().db)


if __name__ == "__main__":
    main()


'''
flake8 output:

firebase_v2.py:25:80: E501 line too long (83 > 79 characters)
#getting value of max temperature from database.

firebase_v2.py:29:80: E501 line too long (83 > 79 characters)
#getting value of min temperature from database.

firebase_v2.py:37:80: E501 line too long (89 > 79 characters)
#format of date being pushed as entry into database.

firebase_v2.py:39:80: E501 line too long (97 > 79 characters)
#format of date being pushed as entry into database.

firebase_v2.py:61:80: E501 line too long (98 > 79 characters)
#Commentation
'''

