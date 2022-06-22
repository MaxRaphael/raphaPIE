
from flask import Flask,render_template,request
from rhino3dm import *

app = Flask(__name__)

 
@app.route('/blogs/<int:id>')
def blogs(id):
    return render_template('template.html', number=id)
 
app.run(host='localhost', port=5000)



