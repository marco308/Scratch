import requests
from bs4 import BeautifulSoup 
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class product:
    # class variable

    def __init__(self, productName, price, date, url = None):
        self.productName = productName
        self.price = price
        self.date = date
        self.url = url

    @staticmethod
    def validateURL(url):
        """
        Helper function used to check if a string is a valid url.

        Args:
            url (str): the url string to be validated

        Returns:
            bool: whether the url is valid or not
        """
        validate = URLValidator()
        try:
            validate(url)
            return True
        except ValidationError:
            return False 

    @staticmethod
    def find_nth(haystack, needle, n):
        """

        Arguments:
            haystack {[str]} -- [the str you want to search]
            needle {[str]} -- [the string you are looking for]
            n {[int]} -- [the nth]

        Returns:
            [int] -- []
        """
        start = haystack.find(needle)
        while start >= 0 and n > 1:
            start = haystack.find(needle, start+len(needle))
            n -= 1
        return start
    
    @staticmethod
    def checkDomain(url, domain): 
        firstPeriod = product.find_nth(url, '.', 1) + 1
        SecondPeriod = product.find_nth(url, '.', 2)
        urlDomain = url[firstPeriod:SecondPeriod]

        if urlDomain == domain:
            print('damain looks good')
            return True
        else:
            print('url domain does not match required domain')
            return False


# Subclass
class waitroseProduct(product):
    # class variables

    def __init__(self, productName, price, date, url):
        super().__init__(productName, price, date, url)

    @classmethod
    def GetWaitrosePrice(cls, url):
        """
        alternative constructor 
        example call: prod1 = product.GetWaitrosePrice('https://www.waitrose.com/ecom/products/warburtons-toastie-thick-sliced-white-bread/026841-13059-13060')
        
        To Do:
        Add Validation 
        """
        validURLFrom = product.validateURL(url) #check that URL has a vaild form (basic form check)
        validDomain = product.checkDomain(url,'waitrose') #check the URL has the domain is waitrose


        if validURLFrom == True and validDomain == True :
            print('good URL')
        
            headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:75.0) Gecko/20100101 Firefox/75.0"}
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')

            productName = soup.find(id="productName").get_text()
            price_raw = soup.findAll("span", {"data-test": "product-pod-price"})
            price = price_raw[0].get_text()
            price = price.replace('£', '' )
            date = None
            return cls(productName,price, date, url)
        else: 
           return print('bad URL'), print( 'URL:' + str(validURLFrom)), print('Domain:' + str(validDomain) )





prod1 = product('apple', '30.00', None, 'html')
print(prod1.__dict__)
print('=============')
print('=============') 

prod1 = waitroseProduct.GetWaitrosePrice('https://www.waitrose.com/ecom/products/warburtons-toastie-thick-sliced-white-bread/026841-13059-13060')

print(prod1.__dict__)