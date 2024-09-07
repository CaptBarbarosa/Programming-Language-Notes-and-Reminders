
"""
import csv
temperatures = []

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)
        temperatures.append(row[1])
temperatures.pop(0)
print(temperatures)
"""


import pandas
pandas.read_csv("weather_data.csv")





