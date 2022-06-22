
from flask import Flask
from rhino3dm import *

app = Flask(__name__)

@app.route('/pleaseWork')
def hello_world():
    return {"5": 45}

