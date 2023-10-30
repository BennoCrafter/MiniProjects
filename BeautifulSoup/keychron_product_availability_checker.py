import json
import sys
import requests
from bs4 import BeautifulSoup

# link of keychron product
# example url:
#url = "https://keychron.com/products/keychron-k1-wireless-mechanical-keyboard" 
if len(sys.argv) == 1:
    url = input("Enter Keychron Product:")
else:
    url = sys.argv[1]

debug = True
available_text = {False: "NOT", True: ""}

try:response = requests.get(url)
except: sys.exit("The given link is invalid!")

soup = BeautifulSoup(response.content, 'html.parser')

# get product name:
product_name = soup.find("title").get_text()
# get product id:
input_element = soup.find('input', {'name': 'product-id'})
if input_element:
    product_id = input_element['value']
else:
    sys.exit("Input element with name 'product-id' not found on the specified URL. Check if the url is correct.")


# get CurrentVariantJson and availability
availability = json.loads(soup.find(id=f"CurrentVariantJson-{product_id}").text)["available"]
if availability == None:
    sys.exit(f"Couldn't get availability of product: {product_id}")

# output info
print(f"The Product:\n\t{product_name} \n\tis \033[1;37m{available_text[availability]} available!\033[0m")

if debug:
    print("\n\n\n")
    print("Debug Infos:")
    print(f"\tProduct id: {product_id}")
    print(f"\tProduct name: {product_name}")
    print(f"\tAvailability: {availability}")

exit(0)