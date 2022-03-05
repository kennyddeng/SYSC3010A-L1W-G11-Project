"""
Flask Server for baby monitor front end GUI
"""
import os
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('index.html')

#if __name__ == '__main__':
    #server_port = os.environ.get('PORT', '8080')
    #app.run(debug=False, port=server_port, host='0.0.0.0')
