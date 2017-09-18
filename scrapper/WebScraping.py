
# coding: utf-8

# In[1]:


import requests


# In[2]:


from bs4 import BeautifulSoup


# In[4]:


import pandas as pd


# In[67]:


r=requests.get("http://www.century21.com/real-estate-offices/chicago-il/LCILCHICAGO/")


# In[68]:


c=r.content


# In[69]:


soup=BeautifulSoup(c,"html.parser")


# In[70]:


all=soup.find_all("div",{"class":"infinite-item office-card clearfix"})


# In[72]:


data_list=[]
for item in all:
        data={}
        data["Address"]=item.find("div",{"class":"office-address"}).text.replace("\r\n","").replace(" ","")
        data["City"]=item.find("div",{"class":"office-city"}).text.replace("\r\n","").replace(" ","")
        data["Phone"]=item.find("div",{"class":"office-phone"}).text.replace("\r\n","").replace("Phone:","").replace("\n","")
        data["Name"]=item.find("a",{"class":"office-name"}).text.replace("\r\n","").replace(" ","")
        
        data_list.append(data)

      


# In[74]:


df=pd.DataFrame(data_list)


# In[76]:


df.to_csv("homes.csv")

