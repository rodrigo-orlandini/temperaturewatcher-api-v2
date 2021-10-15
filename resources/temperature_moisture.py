from datetime import datetime
from flask import request
from flask_restful import Resource

from models.temperature_moisture import TemperatureMoistureModel
from schemas.temperature_moisture import TemperatureMoistureSchema

temperature_moisture_schema = TemperatureMoistureSchema()
temperature_moisture_list_schema = TemperatureMoistureSchema(many=True)

class TemperatureMoisture(Resource):
    @classmethod
    def get(cls):
        return {
            "temperature_moisture": temperature_moisture_list_schema.dump(TemperatureMoistureModel.find_all())
        }, 200

    @classmethod
    def post(cls):
        json = request.get_json()
        temperature_moisture = temperature_moisture_schema.load(json)

        try:
            temperature_moisture.register_date = datetime.now().strftime("%m/%d/%Y")
            temperature_moisture.register_time = datetime.now().strftime("%H:%M:%S")
            temperature_moisture.save_to_database()
            return {"message": "Data registered in database."}, 201
        except:
            return {"message": "Internal Server Error."}, 500