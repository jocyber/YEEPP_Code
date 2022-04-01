from flask import render_template, url_for, request as req, redirect as redi
from flask import request
from app import app
from app.models import Problems
import sqlite3 as sql


#return the index.html file
@app.route('/')
def index():
    #checks templates directory by default
    #Potentially setup a tool that periodically caches this but for now I left it as grabbing everytime...
    connection = sql.connect("database.db")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM problems")
    rows = cursor.fetchall()
    connection.close()

    problems = [Problems(x) for x in rows]

    return render_template("index.html", data=problems) #values=cursor)


#Here is the ajax code should you need it
#This is a mockup for using it when the code is to be run
@app.route('/parse_code',methods=['POST'])
def parse_code():
    if request.method == "POST":
        #Output of AJAX for me to play with
        data = request.form


#function for handling the users code
@app.route('/test', methods=["GET", "POST"])
def testPage():
    #when already loaded
    if req.method == "POST":
        code = req.form["codeEdit"] #name of input from html file
 
        if req.form["action"] == "Run Code":
            #run the 'Run Code' command
            #below return is a test
            return render_template("test.html", data=code);
        else:
            #run the 'submit' command which will modify the database
            pass
    else:
        return render_template("test.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


