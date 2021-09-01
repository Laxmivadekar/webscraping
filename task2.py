import json
import requests
from bs4 import BeautifulSoup
from task1 import scrape_top_movies

def group_by_year(movies):
    l=[]
    l1=[]
    for i in movies:
        l.append(i)
        if i['Year'] not in l1:
            l1.append(i["Year"])
    d={}
    for k in l1:
        l2=[]
        for j in movies:
            year=j["Year"]
            if k==year:
                l2.append(j)
        d[k]=l2
    with open('task2.json','w') as file:
        json.dump(d,file,indent=4)
with open("task1.json","r") as f:
    x=json.load(f)
group_by_year(x)