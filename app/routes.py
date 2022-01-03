from flask import render_template, url_for
from app import app
from app.models import Problems

#return the index.html file
@app.route('/')
def index():
    #checks templates directory by default
    return render_template("index.html")

@app.route('/test')
def testCode():
    return render_template("test.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


