from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

######### Models Start Here #########

#Car Model
class Car(db.Model, SerializerMixin):
    __tablename__ = 'cars'
    
    serialize_rules = ('-car_dealerships', '-created_at', '-updated_at')
    
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
    car_dealerships = db.relationship('DealershipCar', backref = 'car')
    #association proxy
    dealerships = association_proxy('car_dealerships', 'dealership')
    
#Dealership Model
class Dealership(db.Model, SerializerMixin):
    __tablename__ = 'dealerships'

    serialize_rules = ('-car_dealerships', '-created_at', '-updated_at')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    #relationship
    car_dealerships = db.relationship('DealershipCar', backref = 'dealership')
    #association proxy
    cars = association_proxy('car_dealerships', 'car')
    
    
#Dealership Car Model
class DealershipCar(db.Model, SerializerMixin):
    __tablename__ = 'dealership_cars'

    serialize_rules = ('-car.car_dealerships', '-dealership.car_dealerships', '-created_at', '-updated_at')
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    #foreign keys
    dealership_id = db.Column(db.Integer, db.ForeignKey("dealerships.id"))
    car_id = db.Column(db.Integer, db.ForeignKey("cars.id"))

