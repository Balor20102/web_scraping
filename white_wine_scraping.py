import requests
from bs4  import BeautifulSoup
import csv

from get_variable.id_array import id_array
test_array = []
product_link_array = []
photos_array = []

URLS = ["https://weindiele.com/en/white-wine?af=100&ed=1",
        "https://weindiele.com/en/white-wine_s2?af=100&ed=1", 
        "https://weindiele.com/en/white-wine_s3?af=100&ed=1",
        "https://weindiele.com/en/white-wine_s4?af=100&ed=1", 
        "https://weindiele.com/en/white-wine_s5?af=100&ed=1", 
        "https://weindiele.com/en/white-wine_s6?af=100&ed=1", 
        "https://weindiele.com/en/white-wine_s7?af=100&ed=1", 
        "https://weindiele.com/en/white-wine_s8?af=100&ed=1", 
        "https://weindiele.com/en/white-wine_s9?af=100&ed=1", 
        "https://weindiele.com/en/white-wine_s10?af=100&ed=1", 
        "https://weindiele.com/en/white-wine_s11?af=100&ed=1"
        ]

for url in URLS:
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    div_class = soup.find_all('div', class_ = "product-wrapper")

    for div in div_class:
        
        links = div.find_all('a', class_ = 'btn-default')
        results = div.find_all('span', class_ = "value")
        div_photos = div.find_all('div', class_ = 'image-link-wrapper')



        for result in results:
            for id in id_array:
                if result.text == id: 

                    for link in links:


                        product_array = []
                        website_link ="https://weindiele.com/" + link['href']
                        product_link_array.append(product_array)

                        for div_photo in div_photos:

                            photos = div_photo.find_all('img')

                            for photo in photos:
                                if not photo['src'] == "https://weindiele.com/gfx/keinBild.gif":
                                    photo_link = photo['data-src']

                                if photo['src'] == "https://weindiele.com/gfx/keinBild.gif":
                                    photo_link ="https://weindiele.com/gfx/keinBild.gif"

                                product_array = [website_link, photo_link]

                                product_link_array.append(product_array)
\

fields = ['website_product', 'images']

filename = 'white_wine_product_links.csv'

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(product_link_array)

