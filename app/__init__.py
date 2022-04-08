import sqlite3 as sql
from os.path import exists
from flask import Flask

app = Flask(__name__)

from app import routes

if not exists("database.db"):
    connection = sql.connect("database.db")
    cursor = connection.cursor()

    with open("app/static/scripts/creation.sql") as fp:
        command = fp.read()

    command = command.replace("\n","")
    command = command.split(":)")

    for x in command:
        print(x)
        cursor.execute(x)
        connection.commit()

    connection.close()

