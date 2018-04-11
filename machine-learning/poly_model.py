from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from sklearn import linear_model
polynomial= PolynomialFeatures(degree=3)

x=[]
y=[]
with open('multi_poly.txt','r') as f:
	for line in f.readlines():
		data = [float(i) for i in line.strip().split(',')]
		x.append(data[:-1])
		y.append(data[-1])
	

# print X_data
# print y_data
# plt.scatter(x,y)
train_len = int(0.8*len(x))
# print train_len
# exit()
X_train=np.array(x[:train_len])
y_train=np.array(y[:train_len])
test_len=len(x)-train_len
# print X_train
# print y_train

X_test=np.array(x[train_len:])
print X_test
y_test=np.array(y[train_len:])

X_train_tranform = polynomial.fit_transform(X_train)
datapoint=[[0.39,2.78,7.11]]
# datapoint=np.array([0.39,2.78,7.11]).reshape(3,1)

linear_regressor = linear_model.LinearRegression()
linear_regressor.fit(X_train,y_train)


poly_datapoint=polynomial.fit_transform(datapoint)
# print X_train_tranform[0.39,2.78,7.11]
poly_linear_model = linear_model.LinearRegression()
poly_linear_model.fit(X_train_tranform,y_train)
# print linear_regressor.predict(X_test)
print poly_linear_model.predict(poly_datapoint)