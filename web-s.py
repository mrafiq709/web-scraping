from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

prices=[]
driver.get("https://www.thegioididong.com/laptop-ldp")

content = driver.page_source

soup = BeautifulSoup(content)
for price in soup.findAll('strong', attrs={'class':'price'}):
    prices.append(price.text)

df = pd.DataFrame({'Price':prices})
df.to_csv('product.csv', index=False, encoding='utf-8')
