import requests
from bs4 import BeautifulSoup

# write a python code that writes the top 100 movies of all time from empire online into a text file in order
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

top_100 = soup.find_all(name="h3", class_="title")
top_movies = [movies.getText().split(" ", 1)[1] for movies in top_100]
top_bottom = top_movies[::-1]


with open("movie_list.txt", "w", errors="ignore") as data:
    count = 1
    for movie in top_bottom:
        entry = str(count)+") "+ f"{movie}\n"
        data.write(entry)
        count += 1
