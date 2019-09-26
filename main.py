
from flask import Flask, render_template



app=Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

 
@app.route("/location")
def getLocation(): 
	return ("Flask Quebec")

@app.route("/getproduct")
def products():
	return ("List of products")

if __name__ == "__main__":
	app.run(debug=True)