from flask import Flask


app=Flask(__name__)


@app.route("/")
def index():
    return "Hello, burak!"

#create more powerful dynamic web application 
#you can use python all python function in your app 
@app.route("/<string:name>")
def hello(name):
    name=name.upper()
    return name

if __name__== "__main__":
    app.run()