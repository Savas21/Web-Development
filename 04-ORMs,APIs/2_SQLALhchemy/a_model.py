#import SqlAlcehemy
from flask_sqlalchemy import SQLAlchemy


db =SQLAlchemy()

class Flight(db.Model):
    # Define name of the table 
    __tablename__ = "flights"

    # Define Columns in the table 
    id =db.Column(db.Integer , primary_key=True)
    #nullable ==not null
    origin=db.Column(db.String, nullable=False)
    destination=db.Column(db.String, nullable=False)
    duration=db.Column(db.Integer, nullable=False)

class Passenger (db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flighs_id"),nullable=False)

