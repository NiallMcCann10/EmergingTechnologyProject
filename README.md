# EmergingTechnologyProject

<h1>OverView</h1>
This Application is for recognising Hand Written digits on a canvas, and comparing them to that of the MNIST Dataset for classification. This app was developed using a HTML and CSS page to set up a canvas for the user to input their hand drawn digits. With a Tensorflow and keras backend, wrapped up in a Flask Application for deployment.

<h1>Installation</h1>
To clone this repository, simply type into the cmd of your chosen folder git clone https://github.com/NiallMcCann10/EmergingTechnologyProject.git
<br>
To run this application, you require the following:<br>
    Python 3,<br>
    Anaconda,<br>
    Cmder,<br>
    Keras,<br>
    Tensorflow,<br>
    Flask,<br>
    JQuery.<br>
    
Once the repository is cloned, to run the application, Open cmder and in the cmder of the root folder, simply type env FLASK_APP=flaskApp.py flask run<br>

From there you will be prompted to open the webpage http://127.0.0.1:5000/<br>
Using this link, this will run the Application for you on the browser

<h1>Using</h1>
Whilst using the Application the user will see a black canvas 28 X 28 on the screen in front of them. The user is able to draw in the canvas a number of their choosing between 0 and 9. The user is able to draw into the canvas with either the mouse on their PC, or if they have a touchscreen device they will be able to simply use their finger to draw the figure.<br>
Once the figure is drawn into the canvas, the user can simply select the "Predict" button below the canvas. From there the flaskApp will compare the drawn figure to that of the trained MNIST dataset, and return the number that MNIST thinks you have drawn with the certainty of their prediction.<br>
The user is able to clear the screen, without having to reload the entire application each time, simply by selecting the "Clear" button.

<h1>End Product</h1>

![](https://github.com/NiallMcCann10/EmergingTechnologyProject/blob/master/ezgif.com-video-to-gif.gif)


<h1>References</h1>
Links and Videos provided by Dr. Ian McLoughlin of Galway Mayo Institute of Technology.<br>
https://www.codicode.com/art/how_to_draw_on_a_html5_canvas_with_a_mouse.aspx<br>
https://bensonruan.com/handwritten-digit-recognition-with-tensorflow-js/<br>
https://www.youtube.com/watch?v=f6Bf3gl4hWY<br>
https://www.youtube.com/watch?v=wQ8BIBpya2k<br>
