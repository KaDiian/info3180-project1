from . import db
from werkzeug.security import generate_password_hash

class UserProperties(db.Model):
   
    __tablename__ = 'properties'

    propertyid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(250))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.Integer)
    types = db.Column(db.String(20))
    location = db.Column(db.String(200))
    photo = db.Column(db.String(20))

    def __init__(self, title, description, bedrooms, bathrooms, price, types, location, photo):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.types = types
        self.location = location
        self.photo = photo
