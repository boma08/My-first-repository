from bs4 import BeautifulSoup
import lxml

with open("website.html", errors="ignore") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
all_anchor_tags = soup.find_all("a")
print(all_anchor_tags) # prints a list containing all the anchor tags in the html file

for tags in all_anchor_tags:
    print(tags.getText())  # prints only the text in each anchor tag
    print(tags.get("href"))  # prints only the hyper link in each anchor tag
