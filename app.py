from flask import Flask, render_template, make_response, abort
from flask_sqlalchemy import SQLAlchemy
import json
from cities import get_lat_long, request_data
from datetime import datetime 
from database.db import init_db, db, Weather

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/read_all')
def read_all():
	resp = []
	data = Weather.query.all()

	for i in range(0, len(data)):
		data[i].date_created = str(data[i].date_created)
		resp.append((data[i].as_dict()))
	
	return json.dumps(resp)

@app.route('/<city>')
def read_one(city):
	try:
		lat, long = get_lat_long(city)
	except:
		abort(
			404, f"City {city} not found"
		)
		return '<h1>ERROR!</h1><br>Please check the spelling of the city.'
	data = request_data(lat,long).json()['day1']

	if Weather.query.filter_by(city_name=city).all() == []:
		c = Weather(city_name=city, max_temp=data['temperature_max'], min_temp=data['temperature_min'], description=data['icon'], humidity=data['humidity'], wind=data['wind'], wind_dir=data['wind_direction'], sunrise=data['sunrise'], sunset=data['sunset'])
		db.session.add(c)
		db.session.commit()
	
	return make_response(
		f"{city} successfully created", 201
	)

@app.route('/delete/<city>')
def delete(city):
	try:
		Weather.query.filter_by(city_name=city).delete()
		db.session.commit()
		return f'{city} deleted completed successfully'
	except:
		return f'Could not delete {city}'

def main():
    init_db(app)
    app.run() #debug=True
    return app

if __name__ == "__main__":
    main()