import json
import requests
from bs4 import BeautifulSoup
from task1 import scrape_top_movies
from task5 import get_movie_list_details

with open('task5.json','r') as f:
    a=json.load(f)

movies_imfo=a[:30]

def analyse_movies_genre():

    l=[]
    for i in movies_imfo:
        l.append(i['Genre'])



    s_l=[]         #single list
    for i in l:
        if type(i)==list:
            for j in i:
                s_l.append(j)
    r_c=[]      #reducing commas and make as with dublicatesb are there
    for i in s_l:
        str=''
        for j in i:
            if j==',':
                pass
            else:
                str+=j
        r_c.append(str)

    w_d=[]
    for i in r_c:
        if i not in w_d:
            w_d.append(i)
    w_d_l=[]        #without dublicates
    for i in w_d:
        if i=='&':
            pass
        else:
             w_d_l.append(i)

        
    main_dict={}
    for i in w_d_l:
        c=0
        for j in r_c:
            if i==j:
                c+=1
        main_dict[i]=c
    with open('task11.json','w') as f:
        json.dump(main_dict,f,indent=4)
analyse_movies_genre ()



