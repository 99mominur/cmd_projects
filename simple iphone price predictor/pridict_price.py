import pandas
from sklearn.linear_model import LinearRegression

data = pandas.read_csv("iphone_price.csv")
model1 = LinearRegression()


model1.fit(data[["version"]], data[["price"]])

predicted_price = model1.predict([[80]])
print(predicted_price)
