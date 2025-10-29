from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
# so we can save to file:
import joblib

# main testing:
if __name__ == "__main__":
	# load dataset:
	data = pd.read_json("data_v3.json")
	# get train and test datasets
	factors = data[["bedrooms", "electricity", "gas", "water", "gardening", "internet", "tv license", "walk_to_west", "walk_to_east"]]
	prices = data["price"]
	# create and train model:
	model = LinearRegression()
	model.fit(factors, prices)
	# 
	model.fit(factors, prices)
	# model coefficients
	print("Intercept:", model.intercept_)
	print("Coefficients:", model.coef_) 
	# do accuracy on dataset:
	factors["predicted price"] = model.predict(factors)
	# get loss proportional to price
	factors["pred_loss"] = abs((prices - factors["predicted price"]) / prices)
	# show average loss for the model:
	print(factors["pred_loss"].mean())
	# save v3 to file:
	joblib.dump(model, "model_v3.plk")

	# train w/o walking times:
	# load dataset:
	data = pd.read_json("data_v2.json")
	# get train and test datasets
	factors = data[["bedrooms", "electricity", "gas", "water", "gardening", "internet", "tv license"]]
	prices = data["price"]
	# create and train model:
	model = LinearRegression()
	model.fit(factors, prices)
	# 
	model.fit(factors, prices)
	# model coefficients
	print("Intercept:", model.intercept_)
	print("Coefficients:", model.coef_) 
	# do accuracy on dataset:
	factors["predicted price"] = model.predict(factors)
	# get loss proportional to price
	factors["pred_loss"] = abs((prices - factors["predicted price"]) / prices)
	# show average loss for the model:
	print(factors["pred_loss"].mean())
	# save v3 to file:
	joblib.dump(model, "model_v2.plk")
