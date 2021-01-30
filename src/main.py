"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Traveler, Trip, Userpro, Offers

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user/traveler', methods=['POST'])
def handle_Traveler():
    try:
        body= request.get_json()
        if (body["username"] == "" or body["username"] == None ):
            return jsonify({"msg":"correo no es valido"})
        if(body["email"] == "" or body["email"] == None ):
            return jsonify({"msg":"usuario no valido"})
        if(body["password"]=="" or body["password"]== None):
            return jsonify({"msg":"contraseña no valida"})
        new_user = Traveler(username=body["username"],email=body["email"],password=body["password"])
        db.session.add(new_user)
        db.session.commit()
        print(new_user.serialize())
        return jsonify("todo bien"), 200
    except OSError as error:
        return jsonify("Error"), 400

    except KeyError as error:
        return jsonify("Key error" + str(error)), 400
    
@app.route('/viajeros', methods=['GET'])
def get_viajeros():
    total_viajeros = Traveler.query.all()

    response_body = {
        "msg": "estos son todos los viajeros"
    }

    return jsonify(response_body), 200

@app.route('/viajes', methods=['GET'])
def get_viajes():
    total_viajes = Trip.query.all()

    response_body = {
        "msg": "estos son todos los viajes"
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
