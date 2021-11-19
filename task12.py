import json
from bs4 import BeautifulSoup
import requests
movieurl="https://www.rottentomatoes.com/m/toy_story_4"
movieName="toy_story_4"
def scrape_movie_cast(movieName,movieurl):
    url=requests.get(movieurl)
    data=BeautifulSoup(url.text,"html.parser")
    mainDiv=data.find("div",class_="castSection")
    castDiv= mainDiv.find_all("div",class_="media-body")

    dict1={}
    list1=[]
    for i in castDiv:
        a=i.span.text
        b=a.split()
        j= b[0].replace(",","").strip()
        l=" "
        k= b[1].replace(",","").strip()
        h=j+l+ k
        list1.append(h)
    dict1["rt_id"]=list1
    print(dict1)
    with open("task12.json","w")as f:
        json.dump(dict1,f,indent=4)
scrape_movie_cast("toy_story_4","https://www.rottentomatoes.com/m/toy_story_4")

