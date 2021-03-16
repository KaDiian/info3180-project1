from . import db
from werkzeug.security import generate_password_hash

class UserProperties(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(250))
    bedrooms = db.Column(db.Integer(10))
    bathrooms = db.Column(db.Integer(10))
    price = db.Column(db.Integer(50))
    types = db.Column(db.String(20))
    location = db.Columns(db.String(200))
    photo = db.Columns(db.String(20))

    def __init__(self, title, description, bedrooms, bathrooms, price, types, location, photo):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.types = types
        self.location = location
        self.photo = photo
