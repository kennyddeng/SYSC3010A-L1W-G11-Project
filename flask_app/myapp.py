"""
Flask Server for baby monitor front end GUI
"""
import os
from flask import Flask, render_template, request, make_response
from firebase import *
from subprocess import call
from pathlib import Path

app = Flask(__name__)

# Init Variables
firebase = Firebase()
db = firebase.db
storage = firebase.storage
videoPath = str(Path(__file__).parent.absolute()) + "/static/recordings/video/"
audioPath = str(Path(__file__).parent.absolute()) + "/static/recordings/audio/"

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/getdata', methods=['POST', 'GET'])
def get_data():
    # If user selects get data, present form
    if request.method == 'GET':
        return render_template('data_form.html')
    # If user has entered sensorid, display data for that sensor
    elif request.method == 'POST':
        sensor_id = request.form['sensorID']
        data = db.child("sensors").child(sensor_id).child("entries").get().each()
        print("Printing data for sensor #{}".format(sensor_id))
        entries = []
        for entry in data:
            value = str(round(entry.val()["value"], 1)) + "°C"
            date = entry.val()["date"]
            time = entry.val()["time"]
            entries.append({"sensorID": sensor_id,"date": date, "time": time,"value": value})
        entries.reverse() # Show latest entries first
        return render_template('data_form_table.html', entries=entries)

@app.route('/setthreshold', methods=['POST', 'GET'])
def set_threshold():
    # If user selects get data, present form
    if request.method == 'GET':
        return render_template('threshold_form.html')
    # If user has entered sensorid, display data for that sensor
    elif request.method == 'POST':
        min_temp = request.form['min_temp']
        max_temp = request.form['max_temp']
        # Package data
        data = {"min_temperature": min_temp, "max_temperature": max_temp}
        # Update data in DB
        db.child("sensors").child(123).update(data)
        return render_template('threshold_form.html')

@app.route('/livestream')
def livestream():
    return "Hello World"

@app.route('/recording', methods=['POST', 'GET'])
def view_recordings():
    # If user selects recordings, present form
    if request.method == 'GET':
        return render_template('recordings.html')
    # If user has entered sensorid, display data for that sensor
    elif request.method == 'POST':
        rec_type = request.form['type']

        # Display video recording
        if rec_type == "Video":
            # Check if file exists before downloading
            if not os.path.exists(videoPath + "video0.mp4"):
                print("Retrieving video file")
                storage.child("recordings/video/video0.mp4").download(path="/", filename="video0.mp4")
                cmd = "mv video0.mp4 static/recordings/video/video0.mp4"
                call([cmd], shell=True)
            return render_template('recordings.html', video=True)
        # Display audio recording
        elif rec_type == "Audio":
            # Check if file exists before downloading
            if not os.path.exists(audioPath + "test0.wav"):
                print("Retrieving audio file")
                storage.child("recordings/audio/test0.wav").download(path="/", filename="test0.wav")
                cmd = "mv test0.wav static/recordings/audio/test0.wav"
                call([cmd], shell=True)
            return render_template('recordings.html', audio=True)