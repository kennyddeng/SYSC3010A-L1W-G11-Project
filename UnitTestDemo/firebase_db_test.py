from firebase import *
from sense_hat import SenseHat
from datetime import datetime
import unittest

class FirebaseDatabaseTest(unittest.TestCase):
    """
    Firebase database test
    """
    def test_insert_entry(self):
        """
        This test pushes an entry to the Firebase DB that includes the current temperature, date, and time.
        It then reads that same entry from the DB. The test passes if the inserted entry and the read entry are the sane

        Command line run: python3 firebase_db_test.py FirebaseDatabaseTest.test_insert_entry
        """
        db = Firebase().db
        sense = SenseHat()

        # Write to db
        currDateTime = datetime.now()
        date = f"{currDateTime.year:04d}-{currDateTime.month:02d}-{currDateTime.day:02d}"
        time = f"{currDateTime.hour:02d}:{currDateTime.minute:02d}:{currDateTime.second:02d}"

        entry = {"value": round(sense.get_temperature(), 1), "date": date, "time": time}
        db.child("sensors").child(123).child("entries").push(entry)
        entry_write = entry

        # Read from db
        entries = db.child("sensors").child(123).child("entries").get().each()
        latest_entry = entries[-1]
        value = latest_entry.val()["value"]
        date = latest_entry.val()["date"]
        time = latest_entry.val()["time"]
        entry = {"value": value, "date": date, "time": time}
        entry_read = entry

        self.assertTrue(entry_write == entry_read)

if __name__ == "__main__":
    unittest.main()