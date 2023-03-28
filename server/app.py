from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

from models import db, Car, Dealership, DealershipCar

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@app.route('/')
def home():
    return ''

@app.route('/cars', methods=['GET'])
def car():
    cars = Car.query.all()
    cars_dict = [car.to_dict() for car in cars]

    response = make_response(
        jsonify(cars_dict),
        200
    )

    return response

@app.route('/dealership', methods=['GET'])
def dealership():
    dealerships = Dealership.query.all()
    dealerships_dict = [dealership.to_dict() for dealership in dealerships]

    response = make_response(
        jsonify(dealerships_dict),
        200
    )

    return response

@app.route('/dealership_cars', methods=['GET'])
def dealershipCars():
    dealership_cars = DealershipCar.query.all()
    dealership_cars_dict = [dealership_car.to_dict() for dealership_car in dealership_cars]

    response = make_response(
        jsonify(dealership_cars_dict),
        200
    )

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
