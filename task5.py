import requests
import json
from bs4 import BeautifulSoup
from task4 import scrape_top_movie
from task1 import scrape_top_movies

with open('task1.json','r') as f:
    movies_url=json.load(f)
ten_movie=movies_url[:10]
# print(ten_movie)


def get_movie_list_details():
    list_url=[]
    for i in ten_movie:
       for j in i:
           if j=='Url':
               list_url.append(scrape_top_movie(i["Url"]))
    with open('task5.json','w') as f:
        json.dump(list_url,f,indent=4)
    return list_url
get_movie_list_details()