from db import db

class UserModel(db.model):
    __tablename__ = "users"  #table name is items for this class and allof this object
    email = db.Column(db.String(80))
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30))

