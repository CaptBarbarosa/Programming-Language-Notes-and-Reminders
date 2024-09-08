
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
data = pandas.read_csv("weather_data.csv")
print(data)
temps = data["temp"]
print("temps are: ", temps, " its type is: ",type(temps))
temps = temps.to_list()
print(temps)
print(sum(temps)/len(temps))






