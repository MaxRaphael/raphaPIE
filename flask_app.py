
from flask import Flask,render_template,request
from rhino3dm import *

app = Flask(__name__)

 
@app.route('/')
def blogs(id):
    return render_template('template.html', number=id)

if __name__ == '__main__':
    app.run()
 




