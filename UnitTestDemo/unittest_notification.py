from firebase import *
#from firebase_v2 import *
import pyrebase
from sense_hat import SenseHat
import time
from datetime import datetime
from notify import *
from twilio.rest import Client ## pip install twilio
import unittest


class TestNotificationFirebase(unittest.TestCase):
    
    #"""
    #Pi can send notifcation when a temperature threshold is triggered
    #Command Line: python3 unittest_notification.py TestNotificationFirebase.test_notification
    #"""
    
    def test_notification(self):
        
        db = Firebase().db
        notify = Notify()
        curr_temp = 37
        data = {"min_temperature": 39, "max_temperature": 35}
        db.child("sensors").child(123).update(data)
        entry = db.child("sensors").child(123).child("max_temperature").get()
        max_temperature = entry.val()
        entry = db.child("sensors").child(123).child("min_temperature").get()
        min_temperature = entry.val()
        
        if curr_temp > max_temperature:
            msg = "temperature above threshold"
            status = notify.notify_users(msg=msg, users=3)
                
            
        elif curr_temp < min_temperature:
            msg = "temperature below threshold"
            status = notify.notify_users(msg=msg, users=3)
        
        
        self.assertEqual(status[0], "queued")

if __name__ == '__main__':
    #notify = Notify()
    #user = 3
    unittest.main()