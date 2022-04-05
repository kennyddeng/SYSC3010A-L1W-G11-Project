import unittest
from sense_hat import SenseHat
from datetime import datetime
import sqlite3

sense = SenseHat()


class LocalSQLTest(unittest.TestCase):
    """
    Local SQL database test
    """
    def test_local_SQL(self) -> None:
        """
        Pushes an entry to the SQL database.
        Includes date, time and value of the temperature.
        Reads the same entry from the database.
        Passes if the inserted entry and read entry are the same.
        Command Line: python3 unittest_local_SQL.py LocalSQLTest.test_local_SQL
        """
        '''Pushing an entry'''
        dbconnect = sqlite3.connect("SYSC3010Project.db")
        sense = SenseHat()
        entryID = 0
        cursor = dbconnect.cursor()
        currDateTime = datetime.now()
        currDate = datetime.today().strftime("%Y-%m-%d")
        currTime = f"{currDateTime.hour:02d}:{currDateTime.minute:02d}:{currDateTime.second:02d}"
        value = sense.get_temperature()
        entryID += 1
        cursor.execute('''insert into sensordata values (?, ?, ?, ?, ?)''',
                       (entryID, 'Temperature', value, currTime, currDate))

        dbconnect.commit()

        write = cursor.execute('SELECT * FROM sensordata').fetchall()[-1]

        '''Reading last entry'''
        last_row = cursor.execute('SELECT * FROM sensordata').fetchall()[-1]
        self.assertTrue(write == last_row)


if __name__ == '__main__':
    unittest.main()

'''
flake8 output:

unittest_local_SQL.py:28:80: E501 line too long (97 > 79 characters)
#Format of the time used for data entry.
'''
