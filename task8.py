import requests
from bs4 import BeautifulSoup
import json
import os
from task1 import scrape_top_movies
from task4 import scrape_top_movie

with open('task1.json','r') as f:
    a=json.load(f)
movies_data=a

def get_movie_list_details(movie_data):
    movie_list = []
    for i in movies_data:
        path="/home/dell/Desktop/webscraping/1.txt"+i["Moviename"]+".text"

        if os.path.exists("file.json"):
            pass
        else:
            create=open("/home/dell/Desktop/webscraping/1.txt"+i["Moviename"]+".text","w")
            # create=open(i["movieName"]+".text","w")
            url=requests.get(i["Url"])
            create1=create.write(url.text)
            create.close()
        #     a=scrape_top_movie((i["Moviename"],i["Url"]))
        #     movie_list.append(a)
        # with open("task5.json","w+") as file5:
        #     json.dump(movie_list,file5,indent=4)
        #     print(movie_list)
get_movie_list_details(movies_data)