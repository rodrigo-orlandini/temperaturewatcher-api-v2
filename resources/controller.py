from flask import request
from flask_restful import Resource

from models.controller import ControllerModel
from schemas.controller import ControllerSchema

controller_schema = ControllerSchema()

class Controller(Resource):
    @classmethod
    def get(cls):
        return {
            "controller": controller_schema.dump(ControllerModel.find_last())
        }, 200

    @classmethod
    def post(cls):
        json = request.get_json()
        data = controller_schema.load(json)

        try:
            controller = ControllerModel(**data)
            controller.save_to_database()
            return {"message": "Controller updated in database."}, 201
        except:
            return {"message": "Internal Server Error."}, 500