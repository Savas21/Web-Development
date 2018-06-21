
#set Environment for application by export FLASK_APP=hello.py in terminal 
from flask import Flask

app=Flask(__name__)


@app.route("/")

def index():
    return "<h1>Hello ,world! </h1>"


if __name__ == "__main__":
    app.run(debug=True)
#in order to run the app . you should go to the current directory and type "flask run"
