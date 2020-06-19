#!/usr/bin/env python3
# Scikit-learn Iris example

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm

# load data
iris = datasets.load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train Support Vector Machine
classifier = svm.SVC()
print(classifier)
classifier.fit(X_train, y_train)

#Classify the test data
accuracy = classifier.score(X_test, y_test)
print("Accuracy is %0.3f" % accuracy)
print("Process finished")
