from flask import render_template, url_for, request as req, redirect as redi
from flask import request
from app import app
from app.models import Problems, Problem_Info
import sqlite3 as sql
from app.restricted import run_code

import base64
"""Copied from https://nitratine.net/blog/post/how-to-hash-passwords-in-python/
By author unlisted...
Modified for our use"""


import hashlib
import os

"""
salt = os.urandom(32) # Remember this
password = 'password123'
"""

#takes password returns hashednsalted password and salt
def hashnsalt2(password):

    salt = os.urandom(32)

    key = hashlib.pbkdf2_hmac(
      'sha256', # The hash digest algorithm for HMAC
      password.encode('utf-8'), # Convert the password to bytes
      salt, # Provide the salt
     100000 # It is recommended to use at least 100,000 iterations of SHA-256
    )
    return key,salt


def hashnsalt(password,salt):

    salt = salt

    key = hashlib.pbkdf2_hmac(
      'sha256', # The hash digest algorithm for HMAC
      password.encode('utf-8'), # Convert the password to bytes
      salt, # Provide the salt
     100000 # It is recommended to use at least 100,000 iterations of SHA-256
    )
    return key


#print(hashnsalt(password,salt))
#salt = os.urandom(32)
#print(hashnsalt(password,salt))

def page_with_cookie(page):#file
    username = request.cookies.get('username')

    print(username)

    if(username != None):#if cookie exists
        page = page + "_with_login"

    return page + ".html"      

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

    new_page = page_with_cookie("index")
    return render_template(new_page, data=problems) #values=cursor)


#Here is the ajax code should you need it
#This is a mockup for using it when the code is to be run
@app.route('/parse_code',methods=['POST'])
def parse_code():
    if request.method == "POST":
        data = req.get_json()
        code = data["code"]
        problem = data["problem"].split("?")[1]

        #sqlite query to get function name input values and output values from problem
        conn = sql.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM problems WHERE problem_id = {problem}")
        query = cursor.fetchall()[0]
        func = query[0]

        output=run_code(source_code = code, function_name = func, input_values = input_values, output_values = output_values)


        if "not found" in output:
            re_val = output

        elif "syntax" in output:
            re_val = output

        elif "fail" in output:
            re_val = output

        elif "success" in output:
            re_val = output

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

        new_page = page_with_cookie("test")
        return render_template(new_page, descr=problem_info, test=req.args.get("id"))

    #when already loaded
    if req.method == "POST":
        code = req.form["codeEdit"] #name of input from html file
 
        if req.form["action"] == "Run Code":
            #run the 'Run Code' command
            #below return is a test
            return render_template("test.html", data=code)
        else:
            #run the 'submit' command which will modify the database
            pass
    else:
        return render_template("test.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.route("/login", methods=["POST"])
def loginUser():
    try:
        if req.method == "POST":
            conn = sql.connect("database.db")
            cursor = conn.cursor()
            #print("what")
            email = req.form["email"]
            password = req.form["password"]

            cursor.execute("SELECT salt FROM users WHERE email=(?);",([email]))
            salt = base64.urlsafe_b64decode(cursor.fetchall()[0][0])



            password = base64.urlsafe_b64encode(hashnsalt(password, salt))

            cursor.execute(f"SELECT username FROM users WHERE email=(?) and password=(?);",(email,password))
            username = cursor.fetchall()[0][0]
            #print("I'm in boys")
            conn.close()
            return username
    except IndexError:
        conn.close()
        return "failure"

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route("/signUp", methods=["POST"])
def signUpUser():
    try:
        if req.method == "POST":
            conn = sql.connect("database.db")
            cursor = conn.cursor()

            email = req.form["email"]
            password = req.form["password"]
            username = req.form["username"]
            password, salt = hashnsalt2(password)

            password, salt = base64.urlsafe_b64encode(password), base64.urlsafe_b64encode(salt)

            #print(f"INSERT INTO users (full_name, country_code, salt, password, username, email) VALUES ('uu', 0, (?), (?), (?), (?));"
             #     ,(salt,password,username,email))

            cursor.execute(f"INSERT INTO users (full_name, country_code, salt, password, username, email) VALUES ('uu', 0, (?),(?),(?),(?) );",
                           (salt,password,username,email))
            conn.commit()

            return "success"
    except IndexError:
        conn.close()
        return "failure"




