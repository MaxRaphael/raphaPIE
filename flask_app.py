
from flask import Flask,render_template,request
from rhino3dm import *

 
app = Flask(__name__)
 
@app.route('/form')
def form():
    dir = "/home/MaxRaphael/raphaPIE/form.html"
    return render_template(dir)
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    dir = "/home/MaxRaphael/raphaPIE/data.html"
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template(dir,form_data = form_data)

if __name__ == '__main__':
    app.run()
 




