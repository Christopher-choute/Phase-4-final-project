from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})


db = SQLAlchemy(metadata=metadata)

class Car(db.Model, SerializerMixin):
    __tablename__ = '-cars'
    
    customers = association_proxy('dealership_cars', 'dealerships')
    serialize_rules = ('-dealership_cars', '-dealerships.cars')
    
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String)
    model = db.Column(db.String)
    year = db.Column(db.Integer)
    price = db.Column(db.Integer)
    used = db.Column(db.Boolean)
    image = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
#relationship
    dealerships = db.relationship('Dealership_car', backref = 'car')

class Dealership(db.Model, SerializerMixin):
    __tablename__ = 'dealerships'

    cars = association_proxy('dealership_cars', 'cars')
    serialize_rules = ('-dealership_cars', '-cars.dealerships')


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
#relationship
    dealerships = db.relationship('Dealership_car', backref = 'dealership')

#Dealership Model
class DealershipCar(db.Model, SerializerMixin):
    __tablename__ = 'dealership_cars'
    serialize_rules = ('-dealership.cars', '-car.dealerships', '-car.dealership_cars', '-dealership.dealership_cars')

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

#foreign keys
    dealership_id = db.Column(db.Integer, db.ForeignKey("dealership.id"))
    car_id = db.Column(db.Integer, db.ForeignKey("car.id"))

