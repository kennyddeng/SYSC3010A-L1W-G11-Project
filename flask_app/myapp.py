"""
Flask Server for baby monitor front end GUI
"""
import os
from flask import Flask, render_template, request, make_response
from firebase import *

app = Flask(__name__)

# Init Variables
db = Firebase().db

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
        entries = db.child("sensors").child(sensor_id).child("entries").get().each()
        print("Printing data for sensor #{}".format(sensor_id))
        for entry in entries:
            value = entry.val()["value"]
            date = entry.val()["date"]
            time = entry.val()["time"]
            print("Value: {}, Date: {}, Time: {}".format(value, date, time))
        return render_template('data_form.html')

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
