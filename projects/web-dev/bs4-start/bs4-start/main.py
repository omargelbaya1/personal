from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
contents=response.text


soup=BeautifulSoup(contents,"html.parser")
# print(soup.prettify())

article_names=[]
article_links=[]
article_scores=[]

news = soup.find_all(class_="titleline")

for heading in news:
    link=heading.find(name="a").get("href")
    name=heading.find(name="a").getText()

    article_names.append(name)
    article_links.append(link)


scores = soup.find_all(class_="score")
for score in scores:
    new_score=int(score.getText().split(" ")[0])
    article_scores.append(new_score)

largest_number=max(article_scores)

index_of_highest_number=article_scores.index(largest_number)

print(index_of_highest_number,article_names[28],article_scores[28],article_links[28])

#
# with open("website.html") as f:
#     contents= f.read()
#
# soup =BeautifulSoup(contents,'html.parser')
#
# all_anchor_tags=soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))