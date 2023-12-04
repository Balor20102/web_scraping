import requests
from bs4  import BeautifulSoup
import csv

from get_variable.id_array import id_array
test_array = []
product_link_array = []
product_id_array = []
URLS = ["https://weindiele.com/en/red-wine?af=100&ed=1",
        "https://weindiele.com/en/red-wine_s2?af=100&ed=1",
        "https://weindiele.com/en/red-wine_s3?af=100&ed=1",
        "https://weindiele.com/en/red-wine_s4?af=100&ed=1",
        "https://weindiele.com/en/red-wine_s5?af=100&ed=1",
        "https://weindiele.com/en/red-wine_s6?af=100&ed=1",
        "https://weindiele.com/en/red-wine_s7?af=100&ed=1", 
        "https://weindiele.com/en/red-wine_s8?af=100&ed=1", 
        "https://weindiele.com/en/red-wine_s9?af=100&ed=1", 
        "https://weindiele.com/en/red-wine_s10?af=100&ed=1", 
        "https://weindiele.com/en/red-wine_s11?af=100&ed=1",
        "https://weindiele.com/en/red-wine_s12?af=100&ed=1", 
        "https://weindiele.com/en/red-wine_s13?af=100&ed=1", 
        "https://weindiele.com/en/red-wine_s14?af=100&ed=1", 
        "https://weindiele.com/en/red-wine_s15?af=100&ed=1",
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

filename = 'red_wine_product_links.csv'

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(product_link_array)