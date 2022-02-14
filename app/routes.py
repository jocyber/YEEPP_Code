from flask import render_template, url_for, request as req, redirect as redi
from app import app, db

#return the index.html file
@app.route('/')
def index():
    #checks templates directory by default
    cursor = db.session.execute("select * from problems")
    return render_template("index.html", data=cursor) #values=cursor)

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


