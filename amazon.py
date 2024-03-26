#Some libraries are not used. Just there
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

from time import sleep
import time


browser = webdriver.Chrome()
browser.get("https://www.amazon.com/dp/B010OVOPKA")

#list creation to storing data
title=[]
availability=[]
brand = []
ships_from=[]
sold_by= []
price=[]
price_per_weight =[]
size =[]

#for chaning the pin location
pincode = browser.find_element(By.XPATH,'//*[@id="nav-global-location-popover-link"]')
pincode.click()
sleep(3)

#inputing the pincode
input = browser.find_element(By.XPATH,'//*[@id="GLUXZipUpdateInput"]')
input.send_keys('07054')
sleep(3)

#clicking apply
search_apply = browser.find_element(By.XPATH,'//*[@id="GLUXZipUpdate"]/span/input')
search_apply.click()
sleep(3)

#clicking apply
continue_click = browser.find_element(By.XPATH,'//*[@id="a-popover-3"]/div/div[2]/span')
continue_click.click()
sleep(2)

#finding clickable elements to direct to different product variations

product_types = browser.find_elements(By.CSS_SELECTOR, '#variation_style_name > ul > li')

print("Items variations:"+ str(len(product_types)))
#loop to go through all product variations using click()

for items in product_types:
    items.click()
    sleep(3)
  
    title.append(browser.find_element(By.ID, 'productTitle').text)
    #print('title:',title)
    
    try:
        availability_temp =(browser.find_element(By.XPATH, '//*[@id="availability"]/span').text)  
        availability.append('In stock')
    except NoSuchElementException:
        availability.append('Currently Unavailable')
  
    try:
        ships_from.append(browser.find_element(By.XPATH,'//*[@id="sfsb_accordion_head"]/div[1]/div/span[2]').text)
    except NoSuchElementException:
        ships_from.append('Currently Unavailable')
    
    brand.append(browser.find_element(By.XPATH, '//*[@id="productOverview_feature_div"]/div/table/tbody/tr[1]/td[2]/span').text)
    #print('brand:',brand)
    
    try:
        sold_by.append(browser.find_element(By.XPATH,'//*[@id="sfsb_accordion_head"]/div[2]/div/span[2]').text)
    except NoSuchElementException:
        sold_by.append('Currently Unavailable')
     
    try:
        price_element = browser.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]')
        price_temp = price_element.text.strip().split('\n')
        price.append(price_temp[0] + '.' + price_temp[1])
        price_per_weight.append(price_temp[2] + price_temp[3])
    except NoSuchElementException:
        price.append('Currently Unavailable')
        price_per_weight.append('Currently Unavailable')
    
    size.append(browser.find_element(By.XPATH, '//*[@id="productOverview_feature_div"]/div/table/tbody/tr[2]/td[2]/span').text)
  
    sleep(3)

 
print('title:',title)
print('availability:',availability)
print('brand:',brand)
print('ships_from:',ships_from)
print('sold_by:',sold_by)
print('price:',price)
print('price_per_weight:',price_per_weight)
print('size:',size)

#putting it all in the list
data_list = [title,availability,brand,ships_from,sold_by,price,price_per_weight,size]

#making the data table
df = pd.DataFrame(zip(*data_list),columns = ['title','availability','brand','ships_from','sold_by','price','price_per_weight','size'])

df.index.name = 'pro_id'

#exporting in csv
df.to_csv('product2.csv')
df.to_csv('product.csv')

df.head()







