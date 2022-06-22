
from flask import Flask
from rhino3dm import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return {"5": 45}

@app.route('/URLEnd')
def hello_world():
    return "Another URL"

@app.route('/URLEnd2')
def hello_world():
    return "MOARR URL"


