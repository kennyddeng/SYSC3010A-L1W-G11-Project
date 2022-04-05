"""
Flask Server for baby monitor front end GUI

There are 4 main functions for this GUI
1. "Get Data": The user enters a sensor ID and the GUI displays a table of historical sensor data
2. "Set Threshold": The user enters the maximum and minimum temperature thresholds.
3. "Livestream": The user is redirected to a video livestream.
4. "View Recordings": The user can choose recordings to view from a list of available recordings.
"""
import os
from subprocess import call
from pathlib import Path
from flask import Flask, render_template, request, redirect
import sys
sys.path.append("..")
from Python_Modules.firebase import Firebase

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
        # Get sensor ID
        sensor_id = request.form['sensorID']
        # Get sensor type
        entry1 = db.child("sensors").child(sensor_id).child("type").get()
        sensor_type = entry1.val()
        # Get sensor data from DB
        data = \
            db.child("sensors").child(sensor_id).child("entries").get().each()
        print("Printing data for sensor: {}".format(sensor_id))
        entries = []
        for entry in data:
            if sensor_type == "temperature":
                value = str(round(float(entry.val()["value"]), 1)) + "°C"
            else:
                value = entry.val()["value"]
            date = entry.val()["date"]
            time = entry.val()["time"]
            entries.append({"sensorID": sensor_id, "date": date,
                            "time": time, "value": value})
        entries.reverse()  # Show latest entries first
        return render_template('data_form.html', table=True, entries=entries)


@app.route('/setthreshold', methods=['POST', 'GET'])
def set_threshold():
    # If user selects set threshold, present form
    if request.method == 'GET':
        return render_template('threshold_form.html')
    # If user has entered temperture thresholds, update in DB
    elif request.method == 'POST':
        sensor_id = request.form['sensorID']
        min_temp = int(request.form['min_temp'])
        max_temp = int(request.form['max_temp'])
        # Package data
        data1 = {"min_temperature": min_temp}
        data2 = {"max_temperature": max_temp}
        # Update data in DB
        db.child("sensors").child(sensor_id).update(data1)
        db.child("sensors").child(sensor_id).update(data2)
        return render_template('threshold_form.html')


@app.route('/livestream')
def livestream():
    return redirect("http://192.168.2.106:8000/index.html")


@app.route('/recording', methods=['POST', 'GET'])
def view_recordings():
    # If user selects recordings, present form
    if request.method == 'GET':
        recordings = []
        # Get a list of available recordings from the DB
        entry = db.child("sensors").child("recordings").child("entries").get().each()
        for line in entry:
            recordings.append({"name": line.val()["value"]})
        return render_template('recordings.html', recordings=recordings)
    # If user has selected a recording, retrive and display it
    elif request.method == 'POST':
        # Get recording name
        name = request.form['recording_name']
        # Get a list of available recordings from the DB
        recordings = []
        entry = db.child("sensors").child("recordings").child("entries").get().each()
        for line in entry:
            recordings.append({"name": line.val()["value"], "date":line.val()["date"], "time":line.val()["time"]})
            # Get the date and time for the recording selected by the user
            if line.val()["value"] == name:
                date = line.val()["date"]
                time = line.val()["time"]  
        # Check if file exists before downloading
        if not os.path.exists(videoPath + name):
            print("Retrieving video file")
            # Download recording from storage
            storage.child(f"recordings/video/{name}").download(
                path="/", filename=name)
            # Move file into the designated directory
            cmd = f"mv {name} static/recordings/video/{name}"
            call([cmd], shell=True)
        return render_template('recordings.html', video=True, name=name, recordings=recordings, date=date, time=time)