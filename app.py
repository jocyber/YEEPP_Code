from flask import Flask

app = Flask(__name__)

#return the index.html file
@app.route('/')
def index():
    return "Hello, World"

#only runs if the python file is run directly, not when it's imported
if __name__ == "__main__":
    app.run(debug=True)

