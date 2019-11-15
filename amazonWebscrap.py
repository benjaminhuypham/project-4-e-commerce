import csv 
from bs4 import BeautifulSoup 
import requests 

images = []
titles = []
prices = []
brands = []

for i in range(1,30):
    page = requests.get(f"https://www.newegg.com/Homepage-All-Deals/EventSaleStore/ID-9447/Page-{i}?cm_sp=homepage_dailydeal-_--_-11122019")
    soup = BeautifulSoup(page.text, 'html.parser')
    for item_image in soup.find_all(class_="item-img"):
        for image in item_image.find_all('img'):
            images.append(image['src'])

    for item in soup.find_all(class_="item-title"):
        titles.append(item.get_text())

    for brand in soup.find_all(class_="item-brand"):
        for item in brand.find_all('img'):
            brands.append(item['title'])

    for price in soup.find_all(class_="price-current"):
        for item in price.find_all('strong'):
            prices.append(item.get_text())

print(len(images))
print(len(titles))
print(len(brands))
print(len(prices))

data = [[images[i], titles[i], prices[i], brands[i]] for i in range(len(brands))]

header = ['images', 'titles']

with open('deals.csv', 'wt') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerows(data)
