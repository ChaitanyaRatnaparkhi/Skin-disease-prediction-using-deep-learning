import os
import uuid
import flask
import urllib
# from PIL import Image

from flask import Flask , render_template  , request , send_file



app = Flask(__name__)



@app.route('/')
def home():
        return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug = True)   
