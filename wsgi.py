from app import app

#only runs if the python file is run directly, not when it's imported
if __name__ == "__main__":
    app.run(host='0.0.0.0')

