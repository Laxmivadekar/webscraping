import requests
import json
from bs4 import BeautifulSoup
from task1 import scrape_top_movies
from task4 import scrape_top_movie

with  open("task5.json","r") as f:
    data=json.load(f)

def  analyse_language_and_directors():
    dic={}
    for i in data:
        for Director in i["Director"]:
            dic[Director]={}
    for i in range(len(data)):
        for Director in dic:
            if  Director in data[i]["Director"]:
                for  Language  in data[i]["Language"]:
                    dic[Director][Language]=0
    for i in range(len(data)):
        for Director in dic:
            if  Director in data[i]["Director"]:
                for Language  in data[i]["Language"]:
                    dic[Director][Language]+=1
        with open("task10.json","w") as f:
            json.dump(dic,f,indent=4)


    
   
analyse_language_and_directors()
    