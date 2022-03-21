import pyrebase
from sense_hat import SenseHat
import time
from datetime import datetime

config = {
  "apiKey": "AIzaSyBwivJ2TwbSkOEucx481IcMrZ8PIoY56Gc",
  "authDomain": "fir-test-project-6c2f9.firebaseapp.com",
  "databaseURL": "https://fir-test-project-6c2f9-default-rtdb.firebaseio.com/",
  "storageBucket": "fir-test-project-6c2f9.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
sense = SenseHat()
temp = sense.get_temperature()       
       
def stream_handler(message):
    print(message)
    curr_temp = temp
    if message['path'] == '/max_temperature':
        if curr_temp > message['data']:
            print("temperature above threshold")
                
    elif message['path'] == '/min_temperature':
        if curr_temp < message['data']:
            print("temperature below threshold")
                  

if __name__ == "__main__":
    my_stream =db.child('sensors').child('current').child('threshold').stream(stream_handler) 
        
