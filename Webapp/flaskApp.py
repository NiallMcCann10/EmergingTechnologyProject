#For creating the web app
import flask as fl
#for generating numbers
import numpy as np
#for decoding images
import base64

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
    #Decode the string to an image
    decodedimage = base64.decodestring(theimage)
    #Try to save the image
    with open("theimage.png", "wb") as f:
        f.write(decodedimage)
    return{"message": theimage}