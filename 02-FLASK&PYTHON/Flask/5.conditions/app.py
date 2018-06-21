import datetime


from flask import Flask, render_template

app=Flask(__name__)


@app.route("/")
def index():
    #get the current date through python datetime module 
    now = datetime.datetime.now()
    #set boolean values true or false
    new_year= now.month ==1 and now.day==1
    new_year=True
    return render_template("index.html",new_year=new_year)

if __name__=="__main__":
    app.run(debug=True)