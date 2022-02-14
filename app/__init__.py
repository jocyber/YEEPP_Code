from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils.functions import database_exists 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

from app import routes
from app.models import Problems

#create the database if it doesn't exist already
if not database_exists("sqlite:///database.db"):
    db.create_all()
    #test object
    table_row = Problems(title="YOLOOOO", acceptance=0.0, difficulty="Haarrdd")
    db.session.add(table_row)#insert into the database (problems table)
    db.session.commit()

