#-*-coding=utf-8-*-
import numpy as np
from sklearn import datasets,preprocessing
from sklearn.cross_validation import  train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def lession_4():
    iris = datasets.load_iris()
    iris_X = iris.data
    iris_y = iris.target
    # print(iris_X[:2])
    # print(iris_y)
    X_train,X_test,y_train,y_test = train_test_split(iris_X,iris_y,test_size=0.3)
    knn = KNeighborsClassifier()
    knn.fit(X_train,y_train)
    print(knn.predict(X_test))
    print(y_test)

# dataset usage
def lession_5():
    # db = datasets.load_boston()
    # print(db.data.shape)
    # data_X=db.data
    # data_y=db.target
    # model = LinearRegression()
    # model.fit(data_X,data_y)
    # print(model.predict(data_X[:8]))
    # print(data_y[:8])

    X,y = datasets.make_regression(n_samples=100,n_features=1,n_targets=1,noise=10)

    plt.scatter(X,y)
    plt.show()

def lession_6():
    db = datasets.load_boston()
    #print(db.data.shape)
    data_X=db.data
    data_y=db.target
    model = LinearRegression()
    model.fit(data_X,data_y)
    print(model.coef_)
    print(model.intercept_)
    print(model.score(data_X,data_y))

def lession_7():
    X= np.array([[10,12,2],
              [-1,-9,99],
              [22,33,11]])
    print(X)
    print(preprocessing.scale(X))
    #X,y=make

def main():
    lession_7()



if __name__ == '__main__':
    main()