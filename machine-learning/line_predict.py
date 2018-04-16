from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics as sm
try:
	import cPickle as pickle
except:
	import pickle

x=[]
y=[]
with open('line_data.txt','r') as f:
	line=f.readline()
	while line:
		x.append(float(line.strip().split(',')[0]))
		y.append(float(line.strip().split(',')[1]))
		line=f.readline()

# print X_data
# print y_data
# plt.scatter(x,y)
train_len = int(0.8*len(x))
X_train=np.array(x[:train_len]).reshape(train_len,1)
y_train=np.array(y[:train_len])
test_len=len(x)-train_len
# print X_train
# print y_train

X_test=np.array(x[train_len:]).reshape(test_len,1)
y_test=np.array(y[train_len:]).reshape(test_len,1)

fig=plt.figure(figsize=(10,16))

linear_regressor = linear_model.LinearRegression()
linear_regressor.fit(X_train,y_train)

y_train_predict = linear_regressor.predict(X_train)
plt.plot(X_train,y_train_predict,color='r')

plt.scatter(X_test,y_test,color='b')


y_predict=linear_regressor.predict(X_test)
plt.scatter(X_test,y_predict,color='y')

print 'mean error', round(sm.mean_absolute_error(y_test,y_predict),3)
print 'mean std error', round(sm.mean_squared_error(y_test,y_predict),3)
print 'median middle error', round(sm.median_absolute_error(y_test,y_predict),3)
print 'explain score', round(sm.explained_variance_score(y_test,y_predict),3)

plt.show()

with open('linear_modle.pkl','w') as f:
	pickle.dump(linear_regressor,f)
