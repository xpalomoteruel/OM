from geopy.geocoders import Nominatim
import requests

CITIES = {
    'Barcelona': {'Latitude': 41.3828939, 'Longitude': 2.1774322},
    'Berlin': {'Latitude': 52.5170365, 'Longitude' : 13.3888599},
    'Eindhoven': {'Latitude': 51.4392648, 'Longitude' : 5.478633},
    'Maribor': {'Latitude': 46.5576439, 'Longitude' : 15.6455854},
    'Reus': {'Latitude': 41.1555564, 'Longitude' : 1.1076133}
}

def get_lat_long(loc):
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(loc)

    return location.latitude, location.longitude

def request_data(lat, lon):
    return requests.get("https://api.tutiempo.net/json/?lan=en&apid=zwDX4azaz4X4Xqs&ll=" + str(lat) + "," + str(lon))