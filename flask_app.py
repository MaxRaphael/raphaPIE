
from flask import Flask,render_template,request
from flask_app import app 
from rhino3dm import *
import sys

 
app = Flask(__name__)
 
 
@app.route("/")
def blogs():
    path = "/home/MaxRaphael/raphaPIE/data.html"
    return render_template(path)

if __name__ == '__main__':
    app.run()
 




