import requests
from bs4 import BeautifulSoup 


class product:
    # class variable

    def __init__(self, productName, price, date, url = None):
        self.productName = productName
        self.price = price
        self.date = date
        self.url = url

    @classmethod
    def GetWaitrosePrice(cls, url):
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:75.0) Gecko/20100101 Firefox/75.0"}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        productName = soup.find(id="productName").get_text()
        price_raw = soup.findAll("span", {"data-test": "product-pod-price"})
        price = price_raw[0].get_text()
        price = price.replace('£', '' )
        date = None

        return cls(productName,price, date, url)
       





prod1 = product('apple', '30.00', None, 'html')
print(prod1.__dict__)
print('=============')
print('=============') 

prod1 = product.GetWaitrosePrice('https://www.waitrose.com/ecom/products/warburtons-toastie-thick-sliced-white-bread/026841-13059-13060')

print(prod1.__dict__)