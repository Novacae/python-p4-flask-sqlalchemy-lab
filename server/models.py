from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integar, primary_key=True)
    name = db.Column(db.String, unique=True)
    birthday = db.Column(db.integar,unique=False)

    animals = db.relationship('animals', backref='zookeepers')

    def __repr__(self):
        return f'<Zookeepers name is {self.name}>'

class Enclosure(db.Model):
    __tablename__ = 'enclosures'
    Boolean = bool

    id = db.Column(db.Integar, primary_key=True)
    environment = db.Column(db.string)
    open_to_visitors = db.Column(Boolean)

    animals = db.relationship('animals',backref='animals')


    def __repr__(self):
        return f'<Enclosures name is {self.id}>'



class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integar, primary_key=True)
    name = db.Column(db.String, unique=True)
    species = db.Column(db.String)
    enclosure = db.Column(db.string)

    zookeeper_name = db.Column(db.Integer, db.ForeignKey('zookeepers.name'))


    def __repr__(self):
        return f'<Animals name is {self.name}>'
