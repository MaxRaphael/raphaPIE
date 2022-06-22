
from flask import Flask,render_template,request
from rhino3dm import *

app = Flask(__name__)

 
@app.route('/')
def blogs():
    return render_template('template.html')

if __name__ == '__main__':
    app.run()
 




