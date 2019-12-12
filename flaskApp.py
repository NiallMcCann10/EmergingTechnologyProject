from flask import Flask, render_template
#Creating the Flask App
app = Flask(__name__)
#Adding a route for the webpage
@app.route("/")
def index():
    return render_template("WebApp.html")

if __name__ == "__main__":
    app.run(debug=True)