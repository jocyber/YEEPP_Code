from flask import render_template, url_for, request as req, redirect as redi
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
    print(rows)
    connection.close()

    problems = [Problems(x) for x in rows]

    return render_template("index.html", data=problems) #values=cursor)

#function for handling the users code
@app.route('/test', methods=["GET", "POST"])
def testPage():
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


