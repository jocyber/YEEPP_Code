from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

#not sure what the hell I'm doing here, yet
class Problems(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    acceptance = db.Column(db.Float)
    difficulty = db.Column(db.String(10))

    def __init__(self, title, difficulty):
        self.title = title
        self.difficulty = difficulty

#return the index.html file
@app.route('/')
def index():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

#only runs if the python file is run directly, not when it's imported
if __name__ == "__main__":
    app.run(debug=True)

