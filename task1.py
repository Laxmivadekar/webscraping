import requests
import json
from bs4 import BeautifulSoup
url='https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/'
request=requests.get(url)

soup=BeautifulSoup(request.text,'html.parser')
title=soup.find_all('td',class_='unstyled articleLink')
def scrape_top_movies():
    list1=[]
    maindiv=soup.find('div',class_='container')
    tableBody=maindiv.find('div',class_='panel-body content_body allow-overflow')
    alltrs=tableBody.find_all('tr')
    position=0
    for i in alltrs:
        # list=[]
        allTds= i.find_all('td')
        newDict={}
        main={}
        for j in allTds:
            movieName=i.find('a',class_="unstyled articleLink")['href'][3:]
            newDict['Moviename']=movieName
            rating=i.find('span',class_='tMeterIcon tiny').get_text()[3:][:-1]
            newDict['Rating']=rating 
            year=i.find('a',class_='unstyled articleLink').get_text()[5:-1][-4:]
            newDict['Year']=int(year)
            url=i.find('a',class_='unstyled articleLink')['href']
            url_add='https://www.rottentomatoes.com'+url
            newDict['Url']=url_add 
            newDict['position']=position
        position+=1
        if newDict not in list1:
            list1.append(newDict.copy())
    list2=[]
    for i in list1:
        # print(i)
        if i!={}:
            list2.append(i)
    with open('task1.json','w') as webscraping:
        json.dump(list2,webscraping,indent=4)
scrape_top_movies()