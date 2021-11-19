import json

with open("task4.json","r") as f:
    d=json.load(f)
with open("task12.json","r") as f1:
    d1=json.load(f1)

def get_movie_list_details(data,data1):
    dic=data
    for cast in data1.values():
        dic["Cast"]=cast
   
    with open("task13.json","w") as file:
        json.dump(dic,file,indent=4)
    return dic
    
get_movie_list_details(d,d1)
