from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


class Cow(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    birthdate = db.Column(db.DateTime, nullable=False)
    condition = db.Column(db.String(50), nullable=False)
    weight_mass_kg = db.Column(db.Float, nullable=False)
    weight_last_measured = db.Column(db.DateTime, nullable=False)
    feeding_amount_kg = db.Column(db.Float, nullable=False)
    feeding_cron_schedule = db.Column(db.String(20), nullable=False)
    feeding_last_measured = db.Column(db.DateTime, nullable=False)
    milk_last_milk = db.Column(db.DateTime, nullable=False)
    milk_cron_schedule = db.Column(db.String(20), nullable=False)
    milk_amount_l = db.Column(db.Float, nullable=False)
    has_calves = db.Column(db.Boolean, nullable=False)
