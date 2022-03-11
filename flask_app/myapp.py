"""
Flask Server for baby monitor front end GUI
"""
import os
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/getdata')
def get_data():
    return "Hello World"

@app.route('/setthreshold')
def set_threshold():
    return "Hello World"

@app.route('/livestream')
def livestream():
    return "Hello World"
