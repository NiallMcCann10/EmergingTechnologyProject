#For creating the web app
import flask as fl
#for generating numbers
import numpy as np

#create the flask app
app = fl.Flask(__name__)

#Add a route for the web page
@app.route('/')
def home():
    return app.send_static_file('canvas.html')

#Add a route for generating
@app.route("/uploadimage", methods=['GET', 'POST'])
def uploadimage():
    #Get the image from the request
    theimage = fl.request.values.get("theimage", "")
    #print to the python console
    print(theimage)
    return{"message": theimage}