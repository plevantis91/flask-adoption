"""Models for Adoption Agency"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    """Pet"""
    __tablename__ = "pets"
    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=False, default = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png")
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, name, species, photo_url=None, age=None, notes=None, available=True):
        self.name = name
        self.species = species
        self.photo_url = photo_url
        self.age = age
        self.notes = notes
        self.available = available

    def __repr__(self):
        return f"<Pet {self.name} {self.species}>"
    
def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)