from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, String, Date, Float, Integer
from datetime import datetime

DB_URL = 'sqlite:///./database/weather.db'

db = SQLAlchemy()

''' ******************************** JSON FORMAT ********************************
    "day{1:7}:
        - "date": YYYY-MM-DD
        - "temperature_max": Temp max
        - "temperature_min": Temp min
        - "icon": (sol, lluvia, nubes, etc..)
        - "text": (Despejado, Cielo cubierto, Nubes dispersas, etc..)
        - "humidity": Humedad relativa prevista (60, 35, etc..)
        - "wind": Velocidad del viento (12, 30, 45, etc..)
        - "wind_direction": (Norte, Sur, Nordeste, etc..)
        - "icon_wind": icono representativo de la dirección del viento
        - "sunrise": Formato hora
        - "sunset": Formato hora
        - "moonrise": Formato hora
        - "moonset": Formato hora
        - "moon_phases_icon": icono representativo fase lunar
    ********************************************************************************* '''

class Weather(db.Model):
    id = Column(Integer, primary_key=True)
    city_name = Column(String(200), nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow)
    max_temp = Column(Float(precision=2))
    min_temp = Column(Float(precision=2))
    description = Column(String(100))
    humidity = Column(Integer)
    wind = Column(Float(precision=2))
    wind_dir = Column(String(100))
    sunrise = Column(String(100))
    sunset = Column(String(100))

    def __repr__(self):
        return f'<City ({self.id}, {self.city_name}, {self.date_created}, {self.max_temp}, {self.min_temp}, {self.description}, {self.humidity}, {self.wind}, {self.wind_dir}, {self.sunrise}, {self.sunset}>'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    db.create_all(app=app)