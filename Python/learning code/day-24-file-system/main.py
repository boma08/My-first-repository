x = open("C:/Users/Admin/Desktop/my_file.txt")
contents = x.read()
print(contents)
x.close()

with open("C:/Users/Admin/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# The two code segments does the exact same thing

# to write to a file, you have to open the file using the write mode as seen below
with open("C:/Users/Admin/Desktop/my_file.txt", mode="w") as file:
    contents = file.write("I give hope and solve problems \nI am financially stable \nI am great")
    print(contents)

with open("C:/Users/Admin/Desktop/my_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)  # This block of code prints the initial contents of the file, then
    # Then writes new contents from line 14 into file, then read and print
# A mode="a" would not truncate the file but with append new content to existing contents
# Updates the file
with open("C:/Users/Admin/Desktop/my_file.txt", mode="a") as file:
    contents = file.write("\nThis now has the mode set to 'a'. it updates the file")
    print(contents)
