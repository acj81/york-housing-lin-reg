import openrouteservice
import geopy
from geopy.geocoders import Nominatim
import time

def geocode_address(address, wait=1.1):
	# sleep to avoid timeout issues:
	time.sleep(wait)
	print(".")
	# Geocode addresses to get coordinates (lat, lon):
	geolocator = Nominatim(user_agent="walk_time", timeout=10)
	#origin_location = geolocator.geocode(origin + suffix, addressdetails=True)
	location = geolocator.geocode(address)
	# handle not being able to geocode address:
	if not (location):
		# try geocoding every after 1st comma:
		idx = (address).find(",")
		location = geolocator.geocode(address[idx+1:])
	return location

def walking_time(origin_location, destination, api_keys, wait=1.1):
	# set up gmaps API - this is a private key so use another here if necessary
	suffix = ", York, North Yorkshire, England"
	# geocode addresses:
	destination_location = geocode_address(destination + suffix, wait)

	# if still can't just output:
	if not destination_location:
		print(f"couldn't geolocate {destination}")
		return None

	# OpenRouteService expects coordinates as (lon, lat)
	coords = [
   		 (origin_location.longitude, origin_location.latitude),
		(destination_location.longitude, destination_location.latitude)
	]
	# iterate until either no more keys to use or we get no errors:
	for api_key in api_keys:
		try:
			# attempt to get distance
			ors = openrouteservice.Client(key=api_key)
			# get distance matrix and select walking time in seconds:
			route = ors.directions(coords, profile="foot-walking")
			ret = route['routes'][0]['summary']['duration']
			return ret
		except Exception:
			# try next key
			continue
	# if no valid key found, return None:
	return None

# testing section:

if __name__ == "__main__":
	origin = "University of York, University Rd, Heslington, York YO10 5DD"
	destination = "Heslington, York YO10 5GW"
	walk_time = walking_time(origin, destination)
	print(f"{walk_time:.1f}")
