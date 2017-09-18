import pandas as pd
import requests
from bs4 import BeautifulSoup

result=requests.get("https://www.flipkart.com/search?q=laptop&sid=6bo/b5g&as=on&as-show=on&otracker=start&as-pos=1_1_ic_laptop")

content=result.content
soup=BeautifulSoup(content,"html.parser")
all=soup.find_all("div",{"class":"_1-2Iqu row"})

data_lists=[]
for item in all:
    data={}
    data["Product Name"]=item.find("div",{"class":"_3wU53n"}).text
    data["Product small Desc"] =item.find("div",{"class":"OiPjke"}).text
    data["Product Rating"] =item.find("div",{"class":"hGSR34 _2beYZw"}).text.replace("★","")

    data["Product Price"] =item.find("div",{"class":"_1vC4OE _2rQ-NK"}).text

    li=item.find_all("li", {"class": "tVe95H"})
    specs=""
    for li_item in li:
        print("Specs: "+li_item.text)

        specs+=li_item.text+"\n"

    data["Specs"] = specs
    data_lists.append(data)

    df=pd.DataFrame(data_lists)
    df.to_csv("Product.csv")
