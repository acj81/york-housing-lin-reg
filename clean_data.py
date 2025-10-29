import numpy as np #matrices and data analysis
import pandas as pd # handling data in frames
from sklearn.cluster import KMeans # k means clustering for houses
import matplotlib.pyplot as plt # testing and visualisation
from geopy.geocoders import Nominatim # geocode addresses to get latitude and longitude
import time
import ast
import geocoding

# testing:

if __name__ == "__main__":
	'''
	# geocode the data:
	data = pd.read_json("data_v2.json")
	# walking times to each campus:
	west_location = geocoding.geocode_address("Campus West, Heslington, York YO10 5NA")
	east_location = geocoding.geocode_address("Campus East, Heslington, York YO10 5DD")
	api_keys = [
		"REDACTED",
		"REDACTED"
	]
	data["walk_to_east"] = data["address"].apply(lambda x : geocoding.walking_time(east_location, x , api_keys, wait=5))
	data["walk_to_west"] = data["address"].apply(lambda x : geocoding.walking_time(west_location, x , api_keys, wait=5))
	# save times to json file, can manually clean after this
	data.to_json("data_any_walking.json")
	'''
	# drop all records w/o valid distances:
	data = pd.read_json("data_any_walking.json")
	data = data[data["walk_to_east"].isna() != True]
	data = data[data["walk_to_west"].isna() != True]
	data.to_json("data_v3.json")
	'''
	factors = pd.read_json("shf_2025-07-17.json")
	# convert bills included into usable format:
	for bill in ["electricity", "water", "gas", "gardening", "internet", "tv license"]:
		# apply each as separate column - manually convert -> bool -> int to handle empty lists:
		factors[bill] = factors["bills_included"].apply(lambda x : int(bool(x and bill in x)))
	# save to json:
	factors = factors[["address", "bedrooms", "price", "electricity", "water", "gas", "gardening", "internet", "tv license"]]
	factors.to_json("shf_boolean_bills.json")
	'''
