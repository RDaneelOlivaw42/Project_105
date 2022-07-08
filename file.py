import csv
import pandas as pd
import math

with open("/Users/drpoojayadav/Downloads/Project 105/data.csv", newline = "") as f:
    reader = csv.reader(f)
    data = list(reader)

data1 = data[0]
n = len(data1)

def mean():
    addition = 0

    for num in data1:
        x = int(num)
        addition += x

    mean = addition/n
    return mean

def standard_deviation():
    summation = 0

    for num in data1:
        x = int(num)
        figure = (x - mean())**2
        summation += figure

    precursor = summation/(n - 1)
    standard_deviation = math.sqrt(precursor)
    print(standard_deviation)
        
standard_deviation()