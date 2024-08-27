import requests
from bs4 import BeautifulSoup

answer = input("What year would you like to travel to? Type date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{answer}"
SPOTIFY_CLIENT_ID = "1997be9db6f343d49c7c165f4b6b7ade"
SPOTIFY_CLIENT_SECRET = "fcf8b94b09314154b7bf1aaf00c83955"

response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

top_songs = soup.select("li ul li h3")
song_title = [song.getText().strip() for song in top_songs]
print(song_title)
