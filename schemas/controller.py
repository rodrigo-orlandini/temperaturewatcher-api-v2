from marsh import ma
from models.controller import ControllerModel

class ControllerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ControllerModel
        dump_only = ("id",)