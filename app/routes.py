from flask import render_template, url_for, request as req, redirect as redi
from flask import request
from app import app
from app.models import Problems, Problem_Info
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
    if req.method == 'GET':
        conn = sql.connect("database.db")
        cursor = conn.cursor()

        #here add get title of problem to parse the single output
        id_val = req.args.get('id')
        print(id_val)

        cursor.execute(f"SELECT * FROM problems as p inner join examples as e on p.problem_id=e.problem_id and p.problem_id='{id_val}';")#fill in title
        #Reduces to one example
        row = cursor.fetchall()
        print(row)
        problem_info_list = [Problem_Info(x) for x in row]
        conn.close()

        return render_template("test.html", descr=problem_info_list,test=req.args.get("id"))

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


