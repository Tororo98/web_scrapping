import requests
from bs4 import BeautifulSoup
import re

# define url
url = "https://www.amazon.es/Corsair-Auriculares-Conexiones-Inal%C3%A1mbricas-Compatibilidad/dp/B096KWVQCR/ref=dp_fod_1?pd_rd_w=XSzGX&content-id=amzn1.sym.2a122b7c-99f3-41f5-bc1b-32ebd7a34cde&pf_rd_p=2a122b7c-99f3-41f5-bc1b-32ebd7a34cde&pf_rd_r=GTXM8PC82QXKD4H4604C&pd_rd_wg=AVfwp&pd_rd_r=6b7a1016-eb16-4daf-94cb-b9175a228135&pd_rd_i=B096KWVQCR&psc=1"

# function to get data
def getData(url):
    # define user agent
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

    # get url with headers
    res = requests.get(url, headers=headers, timeout=10)

    # define colors for output
    blue = "\33[1;36m"
    color_reset = "\33[0m"

    try:
        # find relevant data in the page
        soup = BeautifulSoup(res.text, "html.parser")
        productTitle = soup.find("div", id="titleSection").text.strip()
        productPrice = soup.find("div", id="corePriceDisplay_desktop_feature_div").text.strip()[0:6].replace(",", ".")
        shippingCostText = soup.find("div", id="mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE").text.strip()
        shippingCost = re.findall(r'(\d+,\d+)', shippingCostText)[0].replace(",", ".")
        availability = soup.find("div", id="availabilityInsideBuyBox_feature_div").text.strip()
        customersReview = soup.find("div", id="averageCustomerReviews").text.strip()[0:21]

        # calculations
        totalCost = float(productPrice) + float(shippingCost)

        # print out data
        print(blue+"Product title: "+color_reset+productTitle+"\n")
        print(blue+"Product's price: "+color_reset+productPrice+"\n")
        print(blue+"Shipping cost: "+color_reset+shippingCost+"\n")
        print(blue+"Total cost: "+color_reset+str(totalCost)+"\n")
        print(blue+availability+"\n")
        print(blue+"Reviews: "+color_reset+customersReview)

    except Exception as e:
        print("Something went wrong: ", e)

if __name__ == '__main__':
    getData(url=url)
    exit(0)
