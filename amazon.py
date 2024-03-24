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

#Commented out code for a single manual page scroll below
'''print(browser.title) #this gets the product title

title_temp = browser.find_element(By.ID,'productTitle') #Title -01
title = title_temp.text
print(title)

Avail = browser.find_element(By.XPATH, '//*[@id="availability"]/span')
availability= Avail.text.strip() #Availability -02
print(availability)

price_temp = browser.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]') #put . then class name for class
price_temp = price_temp.text.strip()
price_temp = price_temp.split('\n')
print(price_temp)

price = price_temp[0] + '.' + price_temp[1] #price
price_per_weight = price_temp[2]+ price_temp[3] #weight
print(price)
print(price_per_weight)

brand = browser.find_element(By.XPATH,('//*[@id="productOverview_feature_div"]/div/table/tbody/tr[1]/td[2]/span'))
brand = brand.text
print(brand)

ships_from = browser.find_element(By.XPATH,'//*[@id="fulfillerInfoFeature_feature_div"]/div[2]/div/span')
ships_from = ships_from.text
print(ships_from)

sold_by = browser.find_element(By.XPATH,'//*[@id="merchantInfoFeature_feature_div"]/div[2]/div/span')
sold_by = sold_by.text
print(sold_by)


size = browser.find_element(By.XPATH,'//*[@id="productOverview_feature_div"]/div/table/tbody/tr[2]/td[2]/span')
size = size.text
print(size)

print(title,availability,brand,ships_from,sold_by,price,price_per_weight,size)

print("#################")

element = browser.find_element(By.XPATH,'//*[@id="ssf-primary-widget-desktop"]')
title_after_click = element.get_attribute("refererURL")'''

#list creation to storing data
title=[]
availability=[]
brand = []
ships_from=[]
sold_by= []
price=[]
price_per_weight =[]
size =[]

#finding clickable elements to direct to different product variations

product_types = browser.find_elements(By.CSS_SELECTOR, '#variation_style_name > ul > li')

print(len(product_types))

#loop to go through all product variations using click()

for items in product_types:
  items.click()
  #time for page to load
  sleep(2)
  
  title.append(browser.find_element(By.ID,'productTitle').text)
  
  availability.append(browser.find_element(By.XPATH, '//*[@id="availability"]/span').text)
  
  brand.append(browser.find_element(By.XPATH,('//*[@id="productOverview_feature_div"]/div/table/tbody/tr[1]/td[2]/span')).text)
  
  #try except if the product goes out of stock it shows "unavailable"
  try:
    ships_from.append(browser.find_element(By.XPATH,'//*[@id="fulfillerInfoFeature_feature_div"]/div[2]/div/span').text)
  except NoSuchElementException:
    ships_from.append('Currently Unavailable')
    
  try:
    sold_by.append(browser.find_element(By.XPATH,'//*[@id="merchantInfoFeature_feature_div"]/div[2]/div/span').text)
  except NoSuchElementException:
    sold_by.append('Currently Unavailable')
     
  try:
    #cleaning the code
    price_temp = browser.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]').text
    price_temp = price_temp.strip()
    price_temp = price_temp.split('\n')
    price.append(price_temp[0] + '.' + price_temp[1])
    
  except NoSuchElementException:
    price.append('Currently Unavailable')  
    
  try:
    price_per_weight_temp = (browser.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]').text)
    price_per_weight.append(price_temp[2]+ price_temp[3])
    
  except NoSuchElementException:
    price_per_weight.append('Currently Unavailable')   
    
  size.append(browser.find_element(By.XPATH, '//*[@id="productOverview_feature_div"]/div/table/tbody/tr[2]/td[2]/span').text)
  sleep(3)


  
print(title)
print(availability)
print(brand)
print(ships_from)
print(sold_by)
print(price)
print(price_per_weight)
print(size)

#putting it all in the list
data_list = [title,availability,brand,ships_from,sold_by,price,price_per_weight,size]

#making the data table
df = pd.DataFrame(zip(*data_list),columns = ['title','availability','brand','ships_from','sold_by','price','price_per_weight','size'])

df.index.name = 'pro_id'

#exporting in csv
df.to_csv('product.csv')

df.head()







