import os
from flask import Flask
from flask_restful import Api

from resources.controller import Controller
from resources.temperature_moisture import TemperatureMoisture

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_UPDATED_URL', "sqlite:///data.db")
app.config['DEBUG'] = True

api = Api(app)
api.add_resource(Controller, "/controller")
api.add_resource(TemperatureMoisture, "/temperature_moisture")

if __name__ == "__main__":
    from database import db
    db.init_app(app)
    
    if app.config.get("DEBUG"):
        @app.before_first_request
        def create_all_tables():
            db.create_all()

    app.run(debug=True, port=5000)