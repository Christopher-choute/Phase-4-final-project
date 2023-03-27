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
    
    customers = association_proxy('dealerships', 'customer')
    serialize_rules = ('-dealerships', '-customers.cars')
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    dealerships = db.relationship('Dealership', backref = 'car')

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    cars = association_proxy('dealerships', 'cars')
    serialize_rules = ('-dealerships', '-cars.customers')


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone_number = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    dealerships = db.relationship('Dealership', backref = 'customer')

class Dealership(db.Model, SerializerMixin):
    __tablename__ = 'dealerships'
    serialize_rules = ('-customer.cars', '-car.customers', '-customer.dealerships', '-car.dealerships')

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    dealership_id = db.Column(db.Integer, db.ForeignKey("dealership.id"))
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

# Models go here!
