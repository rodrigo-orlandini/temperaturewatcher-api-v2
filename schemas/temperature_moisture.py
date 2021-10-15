from marsh import ma
from models.temperature_moisture import TemperatureMoistureModel

class TemperatureMoistureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TemperatureMoistureModel
        dump_only = ("id", "register_date", "register_time")