import json
from bs4 import BeautifulSoup
from task5 import get_movie_list_details

with open('task5.json','r') as f:
    a=json.load(f)
movies_data=a
def analyse_movies_directors():
    l1=[]
    for i in movies_data:
        if i['Director'] not in l1:
            l1.append(i["Director"])
    i=0
    L=[]                           
    while i<len(l1):
        j=0
        while j<len(l1[i]):
            L.append(l1[i][j])
            j=j+1
        i=i+1

    a=L
    a.insert(11,(a[11][:-1]))
    a.pop(12)

    d={}
    for i in a:
        c=0
        for j in a:
            if i==j:
                c=c+1
        d[i]=c
    with open('task7.json','w') as f:
        json.dump(d,f,indent=4)
        
analyse_movies_directors()

































# {

# "Ankita gole": 2,

# "Hrishikesh Mukherjee": 1,

# "Sanjay Leela Bansali": 2

# }