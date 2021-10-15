from database import db

class ControllerModel(db.Model):
    __tablename__ = "controllers"

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float())
    activated = db.Column(db.Boolean())

    @classmethod
    def find_last(cls) -> "ControllerModel":
        return cls.query.order_by(db.desc(cls.id)).limit(1).first() 

    def save_to_database(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit()