from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import sklearn.naive_bayes as naive
import pandas as pd

from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

############################
######Konstanter############
HeaderLen = 60
Test_size = 0.5

def Naive_Bayes_MultiNominal(dataFrame):
    y = dataFrame.Label
    vector = CountVectorizer()
    X = vector.fit_transform(dataFrame.FileContent)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=Test_size)
    classifier = naive.MultinomialNB()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    printHeader("Naive-Bayes Multinominal")
    printMetrics(y_test, y_pred)
    printStar()

def SVM_RBF_kernel(dataFrame):
    y = dataFrame.Label
    vector = CountVectorizer()
    X = vector.fit_transform(dataFrame.FileContent)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=Test_size)

    classifier = svm.SVC(kernel='rbf', gamma=1,decision_function_shape='ovo', C=1)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    printHeader("SVM with RBF kernel")
    printMetrics(y_test, y_pred)
    printStar()

def SVM_poly(dataFrame,degree):
    y = dataFrame.Label
    vector = CountVectorizer()
    X = vector.fit_transform(dataFrame.FileContent)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=Test_size)

    classifier = svm.SVC(kernel='poly',degree=degree,C=1,decision_function_shape='ovo')
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    printHeader("SVM with poly kernel")
    printMetrics(y_test, y_pred)
    printStar()


def SVM_linear(dataFrame):
    y = dataFrame.Label
    vector = CountVectorizer()
    X = vector.fit_transform(dataFrame.FileContent)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=Test_size)

    classifier = svm.SVC(kernel='linear',C=1,decision_function_shape='ovo')
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    printHeader("SVM with linear kernel")
    printMetrics(y_test, y_pred)
    printStar()

def MaxEnt(dataFrame):
    y = dataFrame.Label
    vector = CountVectorizer()
    X = vector.fit_transform(dataFrame.FileContent)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=Test_size)

    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    printHeader("MaxEnt")
    printMetrics(y_test, y_pred)
    printStar()



def printMetrics(y_test, y_pred):
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))


def printHeader(algName):
    printStar()
    print(" " *(int((HeaderLen / 2) - len(algName)/2)) + algName)
    printStar()
    print("")
    print("")


def printStar():
    print("*" * int(HeaderLen))
