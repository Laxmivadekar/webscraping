import pandas as pd  #pd is unless means when we wanted to use pandas(instead of this we will use pad)
import json
import requests
import csv
from bs4 import BeautifulSoup

url='https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
responce=requests.get(url).content


soup=BeautifulSoup(responce,'html.parser')  #the data should be in the html formate
titles=soup.find_all('td',class_='titleColumn')
ratings=soup.find_all('strong')
images=soup.find_all("img")
movietitle=[]
movieratings=[]
movieyear=[]
movieimages=[]
movie_links=[]
img1=[]

for i in titles:
    l1=i.a
    l2=l1.get('href')
    l3='https://www.imdb.com'+l2+'?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=ea4e08e1-c8a3-47b5-ac3a-75026647c16e&pf_rd_r=GFY6V1XPF6JB2WYY18RB&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_tt_1'
    movie_links.append(l3)

for img in images:
    imgs=img.get('src')
    movieimages.append(imgs)

for tit in titles:
    t=tit.a.text
    movietitle.append(t)
    year=tit.span.text
    movieyear.append(year)

for i in ratings:
    rate=i.text.strip()   #strip is a function used for removing the long spaces
    movieratings.append(rate)

data={"links":movie_links,"images":movieimages,"years":movieyear,"ratings":movieratings}
df=pd.DataFrame(data=data)
d=json.dumps(data)
l=json.loads(d)

with open("moveis.csv","w") as  csv_file:
    write=csv.writer(csv_file)
    write.writerow(images)
    for i in images:
        j=i.img['scr']
        img1.append(j)
    write.writerow(img1)