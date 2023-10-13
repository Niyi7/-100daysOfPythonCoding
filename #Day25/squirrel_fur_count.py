import pandas as pd

data = pd.read_csv("4.2 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])
gray_fur = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_fur = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_fur = len(data[data["Primary Fur Color"] == "Black"])
squirrel_fur = {
    "Fur Color": ["gray", "red", "black"],
    "Count": ([(gray_fur), cinnamon_fur, black_fur]),
}
# print(squirrel_fur)
data = pd.DataFrame(squirrel_fur)
data.to_csv("squirrel_count.csv")
