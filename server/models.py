from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.String(20), nullable=True)
    
    # Modify the backref name to 'caretaker' instead of 'zookeeper'
    caretaker = db.relationship('Animal', backref=db.backref('caretaker', lazy=True))

class Enclosure(db.Model):
    __tablename__ = 'enclosures'
    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(20), nullable=False)
    open_to_visitors = db.Column(db.Boolean, default=False)
    
    # Modify the backref name to 'habitat'
    animals = db.relationship('Animal', backref=db.backref('habitat', lazy=True))
class Animal(db.Model):
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    
    # Modify the backref name to 'animal_enclosure'
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'), nullable=True)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'), nullable=True)
    
    zookeeper = db.relationship('Zookeeper', backref=db.backref('animals', lazy=True))
    enclosure = db.relationship('Enclosure', backref=db.backref('animal_enclosure', lazy=True))
