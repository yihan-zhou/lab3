from flask import Flask, render_template
from flask import request
import joblib

app = Flask(__name__)

@app.route("/")
def indef():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)
