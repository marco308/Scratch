# https://www.youtube.com/watch?v=Bg9r_yLk7VY

import requests
from bs4 import BeautifulSoup 


# url = 'https://www.amazon.co.uk/Laurent-Perrier-Cuvee-Rose-Champagne/dp/B0039NHLES/ref=sr_1_13?crid=TZCBL4GV0EE3&dchild=1&keywords=champagne&qid=1588281435&sprefix=cham%2Caps%2C160&sr=8-13'
# url = 'https://www.amazon.co.uk/Bollinger-Special-Cuv%C3%A9e-Champagne-75cl/dp/B003V3POVS/ref=pd_bxgy_2/258-9388692-0043732?_encoding=UTF8&pd_rd_i=B003V3POVS&pd_rd_r=f364fb00-be3b-4087-ac6c-a30d66e41d46&pd_rd_w=wctHM&pd_rd_wg=Sinkb&pf_rd_p=106f838b-b7d1-46e9-83e0-f70facc857bf&pf_rd_r=QJGC61MK0SQD0P7J0Z38&psc=1&refRID=QJGC61MK0SQD0P7J0Z38'
# url = 'https://www.amazon.co.uk/Bollinger-Rose-Non-Vintage-Champagne/dp/B005VRLJNY'
url = 'https://www.waitrose.com/ecom/products/warburtons-toastie-thick-sliced-white-bread/026841-13059-13060'


# just google 'my user agent' to get this info 
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0"}
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:75.0) Gecko/20100101 Firefox/75.0"}



page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
 
# title = soup.find(id="productTitle")
price = soup.findAll("span", {"class": "pricePerUnit___1L8TG"})



# print(title) 
print(price)
