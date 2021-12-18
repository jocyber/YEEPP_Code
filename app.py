from flask import Flask, render_template, url_for

app = Flask(__name__)

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

