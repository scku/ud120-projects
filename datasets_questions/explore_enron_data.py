#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Data points:{0}".format(len(enron_data)) # 146

n_poi = 0
for i in enron_data:
	if enron_data[i]["poi"]:
		n_poi += 1
print "Number of poi:{0}".format(n_poi) # 18

print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"] # 11
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"] # 103559793
print enron_data["FASTOW ANDREW S"]["total_payments"]
