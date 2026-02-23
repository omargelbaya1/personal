import requests
from bs4 import BeautifulSoup


response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

response.raise_for_status()
contents=response.text

soup=BeautifulSoup(contents,"html.parser")


movies_list=[]

movie_titles = soup.find_all(class_="title",name="h3")

for movies in movie_titles:
   movie=movies.getText()
   movies_list.append(movie)

actual_list=movies_list[::-1]

print(actual_list)


with open("movies.txt","w",encoding="utf-8") as f:
    for i in actual_list:
        f.write(i +"\n")