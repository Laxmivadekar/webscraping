import requests
from bs4 import BeautifulSoup
import json
import os
import time
import random
from task1 import scrape_top_movies
from task5 import get_movie_list_details

with open('task5.json','r') as f:
    a=json.load(f)
movies_data=a
# print(movies_data)
def scrape_movie_details (movie_data):
    for i in movies_data:
        random_sleep=random.randint(1,3)
        path=open('/home/dell/Desktop/webscraping/9.txt'+i['Moviename']+'.text','w')
        a=str(i)
        create=path.write(a)
        time.sleep(random_sleep)
        path.close()
scrape_movie_details(movies_data)

