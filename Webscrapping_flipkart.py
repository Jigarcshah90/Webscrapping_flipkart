#!/usr/bin/env python
# coding: utf-8

# The below is the simple Web Scrapping code written in order to download the mobile related information from the FlipKart Site and save in the excel file locally.

# In[ ]:


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


driver = webdriver.Chrome("C:\\Users\\LENOVO\\Downloads\\chromedriver_win32\\chromedriver")


# In[3]:


driver.get("https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&uniq=&page=1")


# In[4]:


content = driver.page_source
soup = BeautifulSoup(content)


# In[5]:


page_no = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div[1]/div[2]/div[26]/div/div/span[1]').text.split()
page_no = int(page_no[-1])
page_no


# In[6]:


for i in range(1,page_no):
    i=str(i)
    #print("https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&uniq=&page="+i)
    page_link = "https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&uniq=&page="+i
    driver.get(page_link)
    content = driver.page_source
    soup = BeautifulSoup(content)
    products=[] #List to store name of the product
    prices=[] #List to store price of the product
    ratings=[] #List to store rating of the product
    description=[]
    df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings,'desc':description})
    for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
        name=a.find('div', attrs={'class':'_3wU53n'})
        price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
        rating=a.find('div', attrs={'class':'hGSR34'})
        desc=a.find('div',attrs={'class':'_3ULzGw'})
        if name is not None:
            products.append(name.text)
        else: 
            products.append('')
        if price is not None:
            prices.append(price.text)
        else: 
            prices.append('')    
        if rating is not None: 
            ratings.append(rating.text)
        else: 
            ratings.append('')
        if rating is not None:    
            description.append(desc.text)
        else:
            description.append('')    
        df = df.append(pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings,'desc':description}))  #
df.to_csv('products.csv', index=False, encoding='utf-8')    


# In[9]:





# In[ ]:




