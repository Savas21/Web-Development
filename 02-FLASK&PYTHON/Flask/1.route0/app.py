from flask import Flask


app=Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

#creating new route 
@app.route("/savas")
def savas():
    return "Hello ,Savas"

@app.route("/maria")
def maria():
    return "Hello ,Maria "
