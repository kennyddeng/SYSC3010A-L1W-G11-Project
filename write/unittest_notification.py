from firebase import Firebase
from notify import Notify
import unittest


class TestNotificationFirebase(unittest.TestCase):

    """
    Test if PI sends notifcation when change threshold is triggered
    Command Line: python3 unittest_notification.py TestNotificationFirebase.test_notification
    """

    def test_notification(self) -> None:

        db = Firebase().db
        notify = Notify()
        curr_temp = 37
        data = {"min_temperature": 39, "max_temperature": 35}
        db.child("sensors").child(123).update(data)
        entry = db.child("sensors").child(123).child("max_temperature").get()
        max_temperature = entry.val()
        entry = db.child("sensors").child(123).child("min_temperature").get()
        min_temperature = entry.val()

        if curr_temp > max_temperature:  # testing to see if current temperature exceeds max limit
            msg = "temperature above threshold"
            status = notify.notify_users(msg=msg, users=3)

        elif curr_temp < min_temperature:  # testing to see if current temperature is lower than min limit
            msg = "temperature below threshold"
            status = notify.notify_users(msg=msg, users=3)

        self.assertEqual(status[0], "queued")


if __name__ == '__main__':
    unittest.main()


'''
flake8 output:
unittest_notification.py:10:80: E501 line too long (93 > 79 characters)
#Commentation on how to execute unit testing.

unittest_notification.py:25:80: E501 line too long (98 > 79 characters)
#In line comment added to provide clarity of test case.

unittest_notification.py:29:80: E501 line too long (106 > 79 characters)
#In line comment added to provide clarity of test case.
'''
