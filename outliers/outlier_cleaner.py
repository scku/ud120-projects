#!/usr/bin/python

from sklearn.linear_model import LinearRegression

def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    ### your code goes here
    reg = LinearRegression()
    reg.fit(ages, net_worths)

    for age, net_worth, prediction in zip(ages, net_worths, predictions):
        error = abs(net_worth - prediction)
        cleaned_data.append((age, net_worth, error))
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2])
    length = int(.9 * len(predictions))
    return cleaned_data[0:length]

