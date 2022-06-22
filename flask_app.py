
from flask import Flask
from flask import render_template
import request
from rhino3dm import *

app = Flask(__name__)

 
@app.route('/')
def blogs(id):
    return render_template('template.html', number=id)
 




