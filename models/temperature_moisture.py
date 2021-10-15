from typing import List

from database import db

class TemperatureMoistureModel(db.Model):
    __tablename__ = "temperature_moisture"

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float(), nullable=False)
    moisture = db.Column(db.Float(), nullable=False)
    register_date = db.Column(db.String(10), nullable=False)
    register_time = db.Column(db.String(8), nullable=False)
    sensor_id = db.Column(db.Integer, nullable=False)

    @classmethod
    def find_all(cls) -> List["TemperatureMoistureModel"]:
        return cls.query.all()

    def save_to_database(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit()