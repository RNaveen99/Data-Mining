import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import KFold
from sklearn import metrics
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MinMaxScaler

dataset = pd.read_csv('breast_cancer.csv')

print(dataset)

dataset = dataset.drop(['id', 'Unnamed: 32'], axis = 1)
print(dataset)

dataset = dataset.replace('M', 1)
dataset = dataset.replace('B', 0)
print(dataset)

X = dataset.iloc[:, 1:]
Y = dataset.iloc[:, 0]

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 1)


