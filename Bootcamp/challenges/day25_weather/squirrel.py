import pandas

data = pandas.read_csv("Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "scores": [gray, cinnamon, black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")