from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Car, Dealership, Customer

app = Flask(__name__)
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

if __name__ == '__main__':
    app.run(port=5555, debug=True)
