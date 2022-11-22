# https://www.pararius.com/ 
from bs4 import BeautifulSoup
import requests
from csv import writer

url="https://www.pararius.com/apartments/amsterdam"
page=requests.get(url)
# print(page)

soup=BeautifulSoup(page.content,'html.parser')
lists=soup.find_all('section',class_="listing-search-item")

with open('housing.csv','w',encoding='utf8',newline='') as f:
    thewriter=writer(f)
    header=["Title","location","Price","Area"]
    thewriter.writerow(header)
    
    for list in lists:
        title=list.find('a',class_="listing-search-item__link--title").text.replace('\n','')
        locatione=list.find('div',class_="listing-search-item__sub-title").text.replace('\n','')
        price=list.find('div',class_="listing-search-item__price").text.replace('\n','')
        area=list.find('li',class_="illustrated-features__item--surface-area").text.replace('\n','')
        info=[title,locatione,price,area]
        thewriter.writerow(info)
        # print(info)
