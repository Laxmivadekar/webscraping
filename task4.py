import json
import requests
from bs4 import BeautifulSoup
# from task1 import scrape_top_movies

movieurl='https://www.rottentomatoes.com/m/toy_story_4'


def scrape_top_movie(movieurl):
    request=requests.get(movieurl)
    soup=BeautifulSoup(request.text,'html.parser')
    
    
    maindiv=soup.find_all('li',class_='meta-row clearfix')
    moviename=soup.find('h1',class_='scoreboard__title').get_text()
    
    d={}
    d['Moviename']=moviename
    d['Movieurl']=movieurl
    for v in maindiv:
        x=v.get_text().strip()
        y=x.split()

        if y[0]=='Rating:':
            d['Rating']=y[1]
        elif y[0]=='Genre:':
            g=[]
            for i in y:
                if i != 'Genre:':
                    a=i.strip()
                    g.append(a)
            d['Genre']=g
            
        elif y[1]=='Language:':
            list=[] 
            for i in y:
                list.append(i)
            a=list
            
            a.remove('Original')
            if a[0]=='Language:':
                a=[a[1]]
                
            d['Language']=a
        elif y[0]=='Director:':
            di=[]
            for i in y:
                di.append(i)
            di.remove('Director:')
            i=0
            li=[]
            while i<len(di):
                j=0
                a=''
                while j<2:
                    t=i+j
                    a+=di[t]
                    j=j+1
                li.append(a)
                i=i+2
            d['Director']=li
        elif y[0]=='Producer:':
            p=[]
            for i in y:
                p.append(i)
            p.remove('Producer:')
            d['Producer']=p
        elif y[0]=='Runtime:':
            r=[]
            for i in y:
                if i != 'Runtime:':
                    a=i.strip()[:-1]
                    r.append(a)
            a=int(r[0])
            mul=a*60
            b=int(r[1])
            sum_min=mul+b
            d['Runtime']=sum_min
    with open('task4.json','w') as f:
        json.dump(d,f,indent=4)
    return d
scrape_top_movie(movieurl) 


