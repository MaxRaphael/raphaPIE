
from flask import Flask,render_template,request
from rhino3dm import *

 
app = Flask(__name__)
 
 
@app.route("/")
def blogs():
    dir = "/home/MaxRaphael/raphaPIE/form.html"
    return render_template(dir)

if __name__ == '__main__':
    app.run()
 




