import os 

from flask import Flask , render_template , request

from a_model import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv["mysql://root:MyNewPass@server/db"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()