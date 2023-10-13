# # Open a file for reading
# with open("weather_data.csv", "r") as file:
#     # Use .readlines() to read all lines into a list
#     lines = file.readlines()

# # Now, 'lines' is a list where each element is a line from the file
# # You can iterate through the list or access individual lines like this:
# for line in lines:
#     print(line)

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temp = []
#     for row in data:
#         if row[1] != "Temp":
#             temp.append(int(row[1]))
#     print(temp)


import pandas as pd

# reads CSV files using Pandas
data = pd.read_csv("weather_data.csv")

# Prints out the Temperature column as a Pandas Series
# print((data["Temp"]))

# Converts the Pandas DataFrame into a Python Dictionary
data_dict = data.to_dict()
# print(data_dict)

# Converts the Pandas series into a python list
temp_list = data["Temp"].to_list()
# prints as list
# print((temp_list))

# Calculate the Average Temperature
items = 0
for item in temp_list:
    items += item
avg_temp = int(items / len(temp_list))
# print(avg_temp)


# Angela Yu's Solution
average = sum(temp_list) / len(temp_list)
# print(average)

# Her alternative solution
# print(data["Temp"].mean())
# print(data["Temp"].max())

# Get Data in Columns
monday = data[data.Day == "Monday"]
print(monday.Day)
print(monday.Condition)
print(monday.Temp)
# temp = data[data.Temp == data.Temp.max()]
# print(temp.Temp)

# Create a new DataFrame from scratch
data_dict = {"students": ["Kenny", "Jerry", "Sunday"], "scores": [90, 58, 63]}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
