import traceback
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
        data = temperature_moisture_schema.load(json)

        try:
            data["register_date"] = datetime.now().strftime("%m/%d/%Y")
            data["register_time"] = datetime.now().strftime("%H:%M:%S")
            temperature_moisture = TemperatureMoistureModel(**data)
            temperature_moisture.save_to_database()
            return {"message": "Data registered in database."}, 201
        except:
            traceback.print_exc()
            return {"message": "Internal Server Error."}, 500