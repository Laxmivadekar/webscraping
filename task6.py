import json
from bs4 import BeautifulSoup
from task5 import get_movie_list_details


with open('task5.json','r') as f:
    movies_url=json.load(f)
a=movies_url
def analyse_movies_language():
    dic={}
    c=0
    for i in a:
        if i['Language']==['English']:
            c+=1
        else:
            pass
    dic['english']=c
    with open('task6.json','w') as f:
        json.dump(dic,f,indent=4)
analyse_movies_language()













#o/p: {

#     "Hindi": 10,

#     "English": 4,

#     "Malyalam": 4

# }