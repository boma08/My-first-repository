import random
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_score = {name: random.randint(1, 100) for name in names}
print(student_score)

student_dict = {
    "student": ["Angela", "Dave", "Lilly"],
    "score": [56, 76, 98]
}
student_dict_df = pandas.DataFrame(student_dict)
print(student_dict_df)  # Prints out the dataframe in tabular form

for (key, value) in student_dict_df.items():
    print(key)  # prints the column title which is also the key
    print(value)  # prints the contents of the specified column

# Pandas interrow() can be used to access a specific cell/value in a dataframe
for (index, row) in student_dict_df.iterrows():
    # print(index)
    # print(row)
    # print(student_dict_df.student)  # this line and the succeeding line does the same thing
    # print(row.student)
    if row.student == "Dave":
        print(row.score)

