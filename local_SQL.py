import sqlite3
from sense_hat import SenseHat
from time import sleep
from datetime import datetime


sense = SenseHat()
entryID = 0
dbconnect = sqlite3.connect("SYSC3010Project.db")
dbconnect.row_factory = sqlite3.Row
cursor = dbconnect.cursor()

'''
Creates a table in the SQL database with the defined parameters
'''

cursor.execute("DROP TABLE IF EXISTS sensordata")

table = '''CREATE TABLE sensordata(

    entryID INT,
    type TEXT,
    value INT,
    time varchar,
    date varchar
)'''

cursor.execute(table)

'''
Writes to the SQL database sends a sensehat temperature reading.
The time and date are also taken.
'''

while True:
    currDateTime = datetime.now()
    currDate = datetime.today().strftime("%Y-%m-%d")
    currTime = f"{currDateTime.hour:02d}:{currDateTime.minute:02d}:{currDateTime.second:02d}"
    value = sense.get_temperature()
    entryID += 1
    cursor.execute('''insert into sensordata values (?, ?, ?, ?, ?)''',
                   (entryID, 'Temperature', value, currTime, currDate))
    dbconnect.commit()

    for row in cursor:
        print(row['entryID'], row['date'], row['currTime'],
              row['value'], row['temp'])
    sleep(1)

dbconnect.close()

'''
Flake8 output:
local_SQL.py:38:80: E501 line too long (93 > 79 characters)
#Format of the time to be used as an entry.
'''
