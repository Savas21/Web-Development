from flask import Flask , render_template, request

app = Flask (__name__)
#how to grab submitted data from the page
#what methots are , get and post 
#if you try to go to /hello site why it gives you error ?

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method=="GET":
        return "Please submit the form instead"
    else:
        name = request.form.get("name")
        return render_template("hello.html",name=name)

if __name__=="__main__":
    app.run(debug=True)