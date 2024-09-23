import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = data["Primary Fur Color"].to_list()
#print(color)
my_dict = {"color": ["Gray", "Red", "Black", "Cinnamon"]}
my_dict["count"] = []
my_dict["count"].append(color.count("Gray"))
my_dict["count"].append(color.count("Red"))
my_dict["count"].append(color.count("Black"))
my_dict["count"].append(color.count("Cinnamon"))
#print("to_csv is: ",my_dict, " its type is: ",type(my_dict))

df = pd.DataFrame(my_dict)
df.to_csv("exercise_2.csv")

