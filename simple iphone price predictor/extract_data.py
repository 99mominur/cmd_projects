import requests
import re
import csv
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/IPhone"

text = requests.get(url).text.encode("utf-8").decode("ascii", "ignore")

soup = BeautifulSoup(text, "lxml")
table = soup.find("table", class_="wikitable")
rows = table.find_all("tr")[1:]

iphone_price_dict = {}

for row in rows:
    data = row.find_all(["th", "td"])
    try:
        version_text = data[0].a.text.split(" ")[1]
        version = re.sub(r"\D", "", version_text)
        version = int(version)
        # print(version)
        price_text = data[-1].text.split("/")[-1]
        price = re.sub(f"\D", "", price_text)
        price = int(price)
        if version and price > 100:
            # print(version, price)
            iphone_price_dict[version] = price
    except:
        pass


# for key, value in iphone_price_dict.items():
#     print(key, value)


csv_fields = ["version", "price"]

with open("iphne_price.csv", "w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(csv_fields)
    for key, value in iphone_price_dict.items():
        csv_writer.writerow([key, value])

    file.close()
