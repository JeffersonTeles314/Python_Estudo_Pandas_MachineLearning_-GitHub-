from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

DecisionTreeRegressor(random_state=1)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)