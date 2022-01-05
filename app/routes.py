from flask import render_template, url_for, request, redirect
from app import app
from app.models import Problems
import os

#return the index.html file
@app.route('/')
def index():
    #checks templates directory by default
    return render_template("index.html")

#function for handling the users code
@app.route('/test', methods=["GET", "POST"])
def testPage():
    if request.method == "POST":
        code = request.form("codeEdit") #name of input from html file
        #run the code through the sandboxed environment
        return redirect(url_for("test")) #return to the test page
    else:
        return render_template("test.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


