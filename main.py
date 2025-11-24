from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
# so we can import from file:
import joblib


if __name__ == "__main__":
    # load model @ start:
    model = joblib.load("model_v2.plk")
    # get each attribute of the house:
    data = {"bedrooms":0, "electricity":0, "gas":0, "water":0, "gardening":0, "internet":0, "tv license":0}
    questions = [
        "number of bedrooms: ",
        "is electricity included? (1 if true, 0 if false): ",
        "is water included? (1 if true, 0 if false): ",
        "is gas included? (1 if true, 0 if false): ",
        "is gardening included? (1 if true, 0 if false): ",
        "is internet included? (1 if true, 0 if false): ",
        "is tv license included? (1 if true, 0 if false): ",
    ]
    # get responses for each and convert to ints
    for i, x in enumerate(questions):
        ans = int(input(x))
        data[list(data.keys())[i]] = [ans]
    # calculate price:
    data = pd.DataFrame(data)
    price = model.predict(data)
    lower_bound = price / 1.08
    upper_bound = price * 1.08
    print(f"predicted price per week is: {price}\n lower bound: {lower_bound} \n upper bound: {upper_bound}")
