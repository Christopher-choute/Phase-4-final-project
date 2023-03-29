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

@app.route('/cars', methods=['GET', 'POST'])
def car():
    cars = Car.query.all()
    if request.method == 'GET':
        cars_dict = [car.to_dict() for car in cars]

        response = make_response(
            jsonify(cars_dict),
            200
        )

        return response
    

    elif request.method == 'POST':

        try:
            new_car = Car(
                make = request.get_json()['make'],
                model = request.get_json()['model'],
                year = request.get_json()['year'],
                price = request.get_json()['price'],
                image = request.get_json()['image']
            )
            db.session.add(new_car)
            db.session.commit()

            response = make_response(
                jsonify(new_car),
                201
            )

        except ValueError:

            response = make_response(
                {"error": "validation errors"},
                400
            )
    return response


@app.route('/cars/<int:id>', methods=['GET', 'DELETE'])
def carById(id):
    car = Car.query.filter_by(id=id).first()

    if request.method == 'GET':
        if car:
            car_dict = car.to_dict() 

            response = make_response(
                jsonify(car_dict),
                    200
            )
        else:
            response = make_response(
                {"error": "Car not fount"},
                404
            )

        return response
    
    elif request.method == 'DELETE':
        if car:
            db.session.delete(car)
            db.session.commit

            response = make_response(
                {},
                200
            )
        else:
            response = make_response(
                {"error": "Car not fount"},
                404
            )

        return response
    
        
# @app.route('/dealership', methods=['GET'])
# def dealership():
#     dealerships = Dealership.query.all()
#     dealerships_dict = [dealership.to_dict() for dealership in dealerships]

#     response = make_response(
#         jsonify(dealerships_dict),
#         200
#     )

#     return response

# @app.route('/dealership_cars', methods=['GET'])
# def dealershipCars():
#     dealership_cars = DealershipCar.query.all()
#     dealership_cars_dict = [dealership_car.to_dict() for dealership_car in dealership_cars]

#     response = make_response(
#         jsonify(dealership_cars_dict),
#         200
#     )

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
