import requests
from bs4  import BeautifulSoup
import csv

 # read csv file
# open the file in read mode
filename = open('rose_product_links.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
website_urls = []
images_array = []

 
# iterating over each row and append
# values to empty list
for col in file:
    website_urls.append(col['website_product'])
    images_array.append(col['images'])




# get all values from website
all_product =[]
for url, image in zip (website_urls, images_array):

    value_array = []
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    title_div = soup.find("h1", class_ = 'product-title')
    value_array.append(title_div.text)
    print(title_div.text)

    price_div = soup.find("strong", class_ = 'price')
    value_array.append(price_div.text)

    ean_div = soup.find("span", itemprop= 'ean')
    if ean_div == None:
        value_array.append(None)
    else:   
        value_array.append(ean_div.text)

    delivery_div = soup.find("span", class_ = "text-nowrap")
    if delivery_div == None:

        delivery = 'Notify me when this item is available'
    else:
        delivery = delivery_div.text

    value_array.append(delivery)

    table_description = soup.find('div', class_ = 'product-attributes')
    tables_values = table_description.find_all("td")
    for value in tables_values:
        if value.text == 'Category:' or value.text == 'SKU:':
            pass
        else:
            value_text = value.text
            value_replace = value_text.replace(":", "")
            value_array.append(value_replace)

    value_array.append(image)

    all_product.append(value_array)

# create csv file
fields = []

for number in range(0, 15):
    a_key = 'a_key_'+ str(number)
    a_value = 'a_value_'+ str(number)
    fields.append(a_key)
    fields.append(a_value)

rows = all_product

create_filename = "create_rose.csv"

with open(create_filename, 'w', encoding="utf-8") as csvfile:

    csvwriter = csv.writer(csvfile)
     
    # writing the fields
    csvwriter.writerow(fields)
     
    # writing the data rows
    csvwriter.writerows(rows)