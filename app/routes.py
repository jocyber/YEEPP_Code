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
        data = req.get_json()
        #run the code here
        return data

#update like and dislike counters
@app.route('/update_count',methods=['POST'])
def update_count():
    if request.method == "POST":
        data = req.form["data"]
        id = req.form["id"]

        conn = sql.connect("database.db")
        cursor = conn.cursor()

        if data == 'like':
            cursor.execute(f"UPDATE userproblems SET isLike=1 WHERE problem_id = {id};")
            cursor.execute("Commit;")#commit the transaction
            cursor.execute(f"SELECT * from problems where problem_id={id};")
            row = cursor.fetchall()[0]
            num = str(Problems(row).likes)
        elif data == 'dislike':
            cursor.execute(f"UPDATE userproblems SET isLike=0 WHERE problem_id={id};")
            cursor.execute("Commit;")
            cursor.execute(f"SELECT * from problems where problem_id={id};")
            row = cursor.fetchall()[0]
            num = str(Problems(row).dislikes)

        conn.close()

        return num


#function for handling the users code
@app.route('/test', methods=["GET", "POST"])
def testPage():
    if req.method == 'GET':
        conn = sql.connect("database.db")
        cursor = conn.cursor()

        #here add get title of problem to parse the single output
        id_val = req.args.get('id')

        cursor.execute(f"SELECT * FROM problems as p, examples as e on p.problem_id=e.problem_id and p.problem_id='{id_val}';")#fill in title
        #Reduces to one example
        row = cursor.fetchall()[0]
        problem_info = Problem_Info(row)
        conn.close()

        return render_template("test.html", descr=problem_info, test=req.args.get("id"))

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


