from sklearn import datasets
from sklearn.linear_model import LinearRegression

lodata = datasets.load_boston()
data_X = lodata.data
data_Y = lodata.target

model = LinearRegression()
model.fit(data_X, data_Y)
print(model.coef_)
print(model.intercept_)

print(model.score(data_X, data_Y))