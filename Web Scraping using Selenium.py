#!/usr/bin/env python
# coding: utf-8

# In[1]:


#for daraz.pk mobiles
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time
import pandas as pd

DRIVER_PATH = r"C:\Users\shahr\Downloads\Compressed\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(DRIVER_PATH)
query_url="https://www.daraz.pk/smartphones/"
driver.get(query_url)
time.sleep(5)
product_list = driver.find_elements(By.CLASS_NAME,'gridItem--Yd0sa')
#ActionChains(browser).click(element).perform()


product_details=[]
'''
for e in product_list:
    product_title = e.find_elements(By.CLASS_NAME,'title--wFj93')
    product_price = e.find_elements(By.CLASS_NAME,'price--NVB62')
    product_loc_rating = e.find_elements(By.CLASS_NAME,'rateAndLoc--XWchq')
    product_info = [product_title.text, product_price.text, product_loc_rating.text]
    product_details.append(product_info) '''

for e in product_list:
    product_title = driver.find_elements(By.CLASS_NAME,'title--wFj93')
    product_price = driver.find_elements(By.CLASS_NAME,'price--NVB62')
    product_loc_rating = driver.find_elements(By.CLASS_NAME,'rateAndLoc--XWchq')
    product_info = [e.text]
    product_details.append(product_info)

driver.quit()


#extracted data in rown and colums
df = pd.DataFrame(product_details) 

df.columns=['Product Details']
#df.columns=['title', 'price' ,'rating']

#data to excel sheet
from pandas import ExcelWriter

writer=ExcelWriter('Daraz_selenium_mobiles.xlsx')
df.to_excel(writer, index=False, encoding='utf-8')
writer.save()


# In[5]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from time import sleep

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = r"C:\Users\shahr\Downloads\Compressed\chromedriver_win32\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
#driver.quit()
query_url="https://www.daraz.pk/laptops/"
browser.get(query_url)
time.sleep(5)

#products=[]
#product_list = browser.find_elements(By.CLASS_NAME,'gridItem--Yd0sa')

input_src = browser.find_element(By.CLASS_NAME,'search-box__input--O34g')
search_btn = browser.find_element(By.XPATH,"(//button[@class='search-box__button--1oH7'])[1]")


input_src.send_keys("Laptops HP")
sleep(1)
search_btn.click()

#for j in product_list:
    #products.append(j.text)
    #next_btn = browser.find_element(By.XPATH,"//div[@class='title--wFj93']")
    #next_btn.click()


# In[ ]:





# In[15]:


#for naheed.pk mobiles


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time
import pandas as pd

DRIVER_PATH = r"C:\Users\shahr\Downloads\Compressed\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(DRIVER_PATH)
query_url="https://www.naheed.pk/phones-tablets/smartphones"
driver.get(query_url)
time.sleep(5)
product_list = driver.find_elements(By.CLASS_NAME,'product-item-info')
#ActionChains(browser).click(element).perform()


product_details=[]
'''
for e in product_list:
    product_title = e.find_elements(By.CLASS_NAME,'title--wFj93')
    product_price = e.find_elements(By.CLASS_NAME,'price--NVB62')
    product_loc_rating = e.find_elements(By.CLASS_NAME,'rateAndLoc--XWchq')
    product_info = [product_title.text, product_price.text, product_loc_rating.text]
    product_details.append(product_info) '''

for e in product_list:
    product_title = driver.find_elements(By.CLASS_NAME,'product-name')
    product_price = driver.find_elements(By.CLASS_NAME,'price')
    #product_loc_rating = driver.find_elements(By.CLASS_NAME,'rateAndLoc--XWchq')
    product_info = [e.text]
    product_details.append(product_info)

driver.quit()


#extracted data in rown and colums
df = pd.DataFrame(product_details) 

df.columns=['Product Details']
#df.columns=['title', 'price' ,'rating']

#data to excel sheet
from pandas import ExcelWriter

writer=ExcelWriter('Naheed_selenium_update.xlsx')
df.to_excel(writer, index=False, encoding='utf-8')
writer.save()


# In[19]:


#for daraz.pk perfumes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time
import pandas as pd

DRIVER_PATH = r"C:\Users\shahr\Downloads\Compressed\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(DRIVER_PATH)
query_url="https://www.daraz.pk/mens-fragrance/junaid-jamshed/?spm=a2a0e.searchlistcategory.card.1.6de91b65vMlj6z&&from=onesearch_category_10002064"
driver.get(query_url)
time.sleep(5)
product_list = driver.find_elements(By.CLASS_NAME,'gridItem--Yd0sa')
#ActionChains(browser).click(element).perform()


product_details=[]
'''
for e in product_list:
    product_title = e.find_elements(By.CLASS_NAME,'title--wFj93')
    product_price = e.find_elements(By.CLASS_NAME,'price--NVB62')
    product_loc_rating = e.find_elements(By.CLASS_NAME,'rateAndLoc--XWchq')
    product_info = [product_title.text, product_price.text, product_loc_rating.text]
    product_details.append(product_info) '''

for e in product_list:
    product_title = driver.find_elements(By.CLASS_NAME,'title--wFj93')
    product_price = driver.find_elements(By.CLASS_NAME,'price--NVB62')
    product_loc_rating = driver.find_elements(By.CLASS_NAME,'rateAndLoc--XWchq')
    product_info = [e.text]
    product_details.append(product_info)

driver.quit()


#extracted data in rown and colums
df = pd.DataFrame(product_details) 

df.columns=['Product Details']
#df.columns=['title', 'price' ,'rating']

#data to excel sheet
from pandas import ExcelWriter

writer=ExcelWriter('Daraz_selenium_perfumes.xlsx')
df.to_excel(writer, index=False, encoding='utf-8')
writer.save()


# In[20]:


#for naheed.pk perfumes


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time
import pandas as pd

DRIVER_PATH = r"C:\Users\shahr\Downloads\Compressed\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(DRIVER_PATH)
query_url="https://www.naheed.pk/health-beauty/perfumes/men-perfumes?manufacturer=42"
driver.get(query_url)
time.sleep(5)
product_list = driver.find_elements(By.CLASS_NAME,'product-item-info')
#ActionChains(browser).click(element).perform()


product_details=[]
'''
for e in product_list:
    product_title = e.find_elements(By.CLASS_NAME,'title--wFj93')
    product_price = e.find_elements(By.CLASS_NAME,'price--NVB62')
    product_loc_rating = e.find_elements(By.CLASS_NAME,'rateAndLoc--XWchq')
    product_info = [product_title.text, product_price.text, product_loc_rating.text]
    product_details.append(product_info) '''

for e in product_list:
    product_title = driver.find_elements(By.CLASS_NAME,'product-name')
    product_price = driver.find_elements(By.CLASS_NAME,'price')
    #product_loc_rating = driver.find_elements(By.CLASS_NAME,'rateAndLoc--XWchq')
    product_info = [e.text]
    product_details.append(product_info)

driver.quit()


#extracted data in rown and colums
df = pd.DataFrame(product_details) 

df.columns=['Product Details']
#df.columns=['title', 'price' ,'rating']

#data to excel sheet
from pandas import ExcelWriter

writer=ExcelWriter('Naheed_selenium_perfumes.xlsx')
df.to_excel(writer, index=False, encoding='utf-8')
writer.save()


# In[ ]:




