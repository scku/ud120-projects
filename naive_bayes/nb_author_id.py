#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 1 (Naive Bayes) mini-project 

    use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import naive_bayes
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
clf = naive_bayes.GaussianNB()
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s" # 3.3s

t0 = time()
predictions = clf.predict(features_test)
print "training time:", round(time()-t0, 3), "s" # 0.37s

acc = accuracy_score(predictions, labels_test)
print "Accuracy:{0}".format(acc)

#########################################################
