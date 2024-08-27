import pandas

gen_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(gen_data[gen_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(gen_data[gen_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(gen_data[gen_data["Primary Fur Color"] == "Black"])

gen_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

gen_data_frame = pandas.DataFrame(gen_dict)
gen_data_frame.to_csv("squirrel_count.csv")
