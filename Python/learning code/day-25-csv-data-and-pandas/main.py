# with open("weather_data.csv") as data:
#     forcast = data.readlines()
#     print(forcast)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     data_list = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")  # stores the file contents in a variable data, as a pandas object
data_dict = data.to_dict()  # stores pandas object as a dictionary
data_list = data["temp"].to_list()  # stores the specified column contents as list items (use data.temp as alternative)

print(data)  # prints the pandas object to console
print(data_dict)  # prints the dictionary
print(data_list)  # prints the list

# 1 One way of calculating the average temperature
total_temp = 0
for i in data_list:
    total_temp += i
avg_temp = total_temp/len(data_list)
print(avg_temp)

# 2 calculating average temperature using the python sum()
total_temp2 = sum(data_list)
avg_temp2 = total_temp2/len(data_list)
print(avg_temp2)

# 3 using the pandas library to do the same calculation and more
avg_temp3 = data["temp"].mean()  # using the pandas mean() to calculate the average the temp column entries
print(avg_temp3)

max_temp = data["temp"].max()  # using the pandas max() to find the maximum entry of the temp column values
print(max_temp)

# to get a row entry
row_entry = data[data.day == "Monday"]  # assigns the row with day == Monday to row_entry while maintaining column title
print(row_entry)

row_with_max_temp = data[data.temp == data.temp.max()]
print(row_with_max_temp)  # Prints the row entry that has the max temp value

# If we call the pandas object and specify the name of a column, the entire column entry will be printed out example:
print(data.temp)

# If we specify a specific column value in [square brackets] like we did in line 48 and 45, only the row is printed
print(data[data.condition == "Sunny"])  # Here only rows whose condition entry matches the argument passed is printed

# We can assign pandas object (row) to a variable and use that variable to obtain the entry for any of it columns
monday = data[data.day == "Monday"]
print(monday.condition)  # Prints the condition of the row(s) whose day entry is/are Monday
print(monday.temp)  # Prints the temp of the row(s) whose day entry is/are Monday
print(monday.day)  # Prints the day of the row(s) whose day entry is/are Monday

monday_temp_in_fahrenheit = (monday.temp * (9/5)) + 32
print(monday_temp_in_fahrenheit)  # Note: this output is a pandas object type (check the console display)

monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)  # Note: this output is a float type

# Creating a data frame from scratch may be you want to write an output to a data frame
#  Step 1: create your data in a data structure, preferably a dictionary
student_scores_dict = {
    "studnets": ["Boma", "Anny", "James"],
    "scores": [100, 78, 75]
}

# step 2: convert the dictionary into a data frame
student_scores_dataframe = pandas.DataFrame(student_scores_dict)
print(student_scores_dataframe)

#  We can also save the dataframe as a csv file
student_scores_dataframe.to_csv("student_scores.csv")  # look in the folder containing this main.py, you will find
#  the students_scores_dataframe.csv file


