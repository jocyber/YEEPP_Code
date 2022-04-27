from flask import make_response, render_template, url_for, request as req, redirect as redi
from flask import request
from app import app
from app.models import Problems, Problem_Info, User
import sqlite3 as sql
from app.restricted import run_code
from werkzeug.utils import secure_filename
import pandas as pd
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

file_types = set(["jpg", "png", "jpeg"])

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

def get_upload():
    profile_pic = req.cookies.get("profile_pic")
    print(profile_pic)
    
    if profile_pic is not None:
        #print(profile_pic)
        return profile_pic
    return "user.png"

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
    file = get_upload()
    print(problems[0].acceptance)
    return render_template(new_page, data=problems, image=url_for('static', filename=f'images/{file}'))

@app.route('/upload', methods=["POST"])
def upload():
    username = req.cookies.get("username")
    conn = sql.connect("database.db")
    cursor = conn.cursor()  
    cursor.execute(f"SELECT * FROM users WHERE username='{username}';")
    row = cursor.fetchall()[0]

    user = User(row)
    conn.close()

    #file upload
    file = req.files['file']

    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    resp = make_response(render_template("profile.html", data=user, image=url_for('static', filename=f'images/{filename}')))
    resp.set_cookie('profile_pic', filename)
    return resp

#for user profile
@app.route('/profile')
def profile():
    username = req.cookies.get("username")

    conn = sql.connect("database.db")
    cursor = conn.cursor()  
    cursor.execute(f"SELECT * FROM users WHERE username='{username}';")
    row = cursor.fetchall()[0]

    user = User(row)
    conn.close()

    file = get_upload()
    return render_template("profile.html", data=user, image=url_for('static', filename=f'/images/{file}'))
    

#Here is the ajax code should you need it
#This is a mockup for using it when the code is to be run
@app.route('/parse_code',methods=['POST'])
def parse_code():
    if request.method == "POST":
        data = req.get_json()
        code = data["code"]
        problem = data["problem"].split("?id=")[1]

        #sqlite query to get function name input values and output values from problem
        conn = sql.connect("database.db")
        cursor = conn.cursor()

        #print(problem)

        cursor.execute("SELECT input, output, methodHeader FROM examples WHERE problem_id = (?)",(int(problem)))
        examples = cursor.fetchall()

        outputdata = []

        try:
            username = request.cookies.get('username')
            #cursor.close()
            cursor.execute("SELECT user_id FROM users WHERE username = (?)",([username]))
            user_id = cursor.fetchall()[0][0]

            if not os.path.exists(f"user_data/{username}"): os.makedirs(f"user_data/{username}")

            with open(f"user_data/{username}/{problem}.py","w+") as fp:
                fp.write(code)

            cursor.execute("SELECT * FROM userproblems WHERE user_id = (?) AND problem_id = (?)")
            if len(cursor.fetchall()) <1:
                cursor.execute("INSERT INTO userproblems(user_id,problem_id,isFavorite,isComplete) VALUES( (?), (?), 0, 0);",(user_id,int(problem)))

            #TODO implement update existing userproblem
        except:
            pass


        for i in range(len(examples)):
            print(i)
            func = examples[i][2]
            input_values = examples[i][0]
            output_values = examples[i][1]


            output=run_code(source_code = code, function_name = func, input_values = input_values, output_values = output_values)



            
            outputdata.append(output)
                

            if "not found" in output:
                outputdata.append(output)
                break

            elif "syntax" in output:
                outputdata.append(output)
                break

            elif "fail" in output:
                outputdata.append(output)

            elif "success" in output:
                outputdata.append(output)
                conn = sql.connect("database.db")
                cursor = conn.cursor()

                cursor.execute("UPDATE userproblems SET isComplete = 1;")
                cursor.execute("Commit;")
                conn.close()

        return outputdata[0]

#update like and dislike counters
@app.route('/update_count',methods=['POST'])
def update_count():
    if request.method == "POST":
        data = req.form["data"]
        id = req.form["id"]
        num=0
        conn = sql.connect("database.db")
        cursor = conn.cursor()
        print("why me")
        cursor.execute(f"SELECT * from problems where problem_id={id};")
        initial_result = cursor.fetchall()[0]
        initial_problem = Problems(initial_result)
        try:
            conn.execute("SELECT user_id FROM users WHERE username = (?)",(int(req.form["username"])))
            user_id = conn.fetchall()[0][0]
        except:
            print("Error",req.form["username"])
            return {"likes":initial_problem.likes, "dislikes": initial_problem.dislikes}

        if data == 'like':
            cursor.execute(f"UPDATE userproblems SET isLike=1 WHERE problem_id = (?) AND user_id = (?);",(id,user_id))
            cursor.execute("Commit;")#commit the transaction
            cursor.execute(f"SELECT * from problems where problem_id={id};")
            row = cursor.fetchall()[0]
            prob = Problems(row)
            num = str(prob.likes)
        elif data == 'dislike':
            cursor.execute(f"UPDATE userproblems SET isLike=0 WHERE problem_id=(?) AND user_id = (?);",(id,user_id))
            cursor.execute("Commit;")
            cursor.execute(f"SELECT * from problems where problem_id={id};")
            row = cursor.fetchall()[0]
            prob = Problems(row)
            num = str(prob.dislikes)
        conn.close()
        prob = {"likes":prob.likes,"dislikes":prob.dislikes}
        print(prob)
        print(num)
        return  str(num)


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
        print(row)
        print(row[-1])
        problem_info = Problem_Info(row)

        try:
            print("trying ")
            username = req.cookies.get("username")

            if username is None:
                code = ""
            elif os.path.exists(f"user_data/{username}/{id_val}.py"):
                with open(f"user_data/{username}/{id_val}.py","r") as fp:
                    code = fp.read()
                    print("I got thereeed")
            else:
                code = ""
        except:
            code = ""

        conn.close()

        new_page = page_with_cookie("test")

        file = get_upload()
        return render_template(new_page, descr=problem_info, code = code ,test=req.args.get("id"), image=url_for('static', filename=f'/images/{file}'))


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




