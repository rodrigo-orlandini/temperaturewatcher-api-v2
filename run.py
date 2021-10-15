from app import app
from database import db

db.init_app(app)

@app.before_first_request
def create_all_tables():
    db.create_all()