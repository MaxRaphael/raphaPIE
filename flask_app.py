from flask import Flask, request
import pandas as pd
import numpy as np
import ghhops_server as hs
app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/cv_ShapeIdentifier",
    name="cv_ShapeIdentifier",
    description="This tool identifies a shape and then draws it into grasshopper",
    inputs=[
        hs.HopsNumber("Shape"),
    ],
    outputs=[hs.HopsPoint("Output")]
)

@app.route('/')
def cv_ShapeIdentifier():
    return "hi"
    

   
if __name__ == '__main__':
    app.run()
