from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
scores = soup.find_all(name="span", class_="score")
article_text = []
article_link = []
article_score = [int(score.getText().split()[0]) for score in scores]


for article in articles:
    text = article.getText()
    article_text.append(text)
    link = article.get("href")
    article_link.append(link)


print(article_text[article_score.index(max(article_score))])








