
from flask import Flask
from rhino3dm import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return {"5": 45}

@app.route('/URLEnd')
def another():
    return "Another URL"

@app.route('/URLEnd2')
def more():
    return "MOARR URL"


