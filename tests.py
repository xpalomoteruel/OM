import unittest
from cities import get_lat_long, CITIES

######################## GEOPY ##########################
# Barcelona: Latitude = 41.3828939, Longitude = 2.1774322
# Berlin: Latitude = 52.5170365, Longitude = 13.3888599
# Eindhoven: Latitude = 51.4392648, Longitude = 5.478633 
# Maribor: Latitude = 46.5576439, Longitude = 15.6455854
# Reus: Latitude = 41.1555564, Longitude = 1.1076133
#########################################################

class Test(unittest.TestCase):

	def test_lat_long_berlin(self):
		lat, long = get_lat_long('Berlin')
		self.assertEqual(lat, CITIES['Berlin']['Latitude'], msg="Berlin's latitude incorrect")
		self.assertEqual(long, CITIES['Berlin']['Longitude'], msg="Berlin's Longitude incorrect")
	
	def test_lat_long_reus(self):
		lat, long = get_lat_long('Reus')
		self.assertEqual(lat, CITIES['Reus']['Latitude'], msg="Reus's latitude incorrect")
		self.assertEqual(long, CITIES['Reus']['Longitude'], msg="Reus's Longitude incorrect")

	def test_lat_long_eindhoven(self):
		lat, long = get_lat_long('Eindhoven')
		self.assertEqual(lat, CITIES['Eindhoven']['Latitude'], msg="Eindhoven's latitude incorrect")
		self.assertEqual(long, CITIES['Eindhoven']['Longitude'], msg="Eindhoven's Longitude incorrect")

	def test_lat_long_maribor(self):
		lat, long = get_lat_long('Maribor')
		self.assertEqual(lat, CITIES['Maribor']['Latitude'], msg="Maribor's latitude incorrect")
		self.assertEqual(long, CITIES['Maribor']['Longitude'], msg="Maribor's Longitude incorrect")

	def test_lat_long_barcelona(self):
		lat, long = get_lat_long('Barcelona')
		self.assertEqual(lat, CITIES['Barcelona']['Latitude'], msg="Barcelona's latitude incorrect")
		self.assertEqual(long, CITIES['Barcelona']['Longitude'], msg="Barcelona's Longitude incorrect")
	
if __name__ == '__main__':
	unittest.main()