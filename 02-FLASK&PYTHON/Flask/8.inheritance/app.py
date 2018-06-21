from flask import Flask , render_template

app= Flask(__name__)

#how to make template inheritance to layout.html
#when there is a repetition in different pages just use this technic
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("more.html")


if __name__=="__main__":
    app.run(debug=True)