from flask import Flask , render_template

app=Flask(__name__)

@app.route("/")
def index():
    headline="Hello,savas!"
    return render_template("index.html",headline=headline)

#you dont have to define seperately two different headline 
@app.route("/bye")
def bye():
    headline="Goodbye, savas!"
    return render_template("index.html",headline=headline)

if __name__=="__main__" :
    app.run(debug=True)


