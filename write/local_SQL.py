import sqlite3
from sense_hat import SenseHat
from time import *
from datetime import *

sense = SenseHat()
entryID = 0
dbconnect = sqlite3.connect("SYSC3010Project.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();

    
cursor.execute("DROP TABLE IF EXISTS sensordata")

table = '''CREATE TABLE sensordata(

    entryID INT,
    type TEXT,
    value INT,
    time varchar,
    date varchar
)'''

cursor.execute(table)

while True:
        
    currDateTime = datetime.now()

    currDate = datetime.today().strftime("%Y-%m-%d")

    currTime = f"{currDateTime.hour:02d}:{currDateTime.minute:02d}:{currDateTime.second:02d}"
        
    value = sense.get_temperature()
    
    entryID += 1;
    cursor.execute('''insert into sensordata values (?, ?, ?, ?, ?)''', (entryID, 'Temperature', value, currTime, currDate));
    dbconnect.commit();

    for row in cursor:
        print(row['entryID'], row['date'], row['currTime'], row['value'], row['temp'] );
    sleep(1)
    
dbconnect.close();
