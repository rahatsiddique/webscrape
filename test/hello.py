
import urllib
from bs4 import BeautifulSoup

quote_page = "https://www.bloomberg.com/quote/SPX:IND"

page = urllib.request.urlopen(quote_page) #query the website and return the html to the variable page

soup = BeautifulSoup (page, "html.parser") #what do i do here to conenct it to the html file?

name_box = soup.find("h1", attrs={"class": "name"})

name = name_box.text.strip()

print (name)

price_box = soup.find("div", attrs={"class":"price"})
price = price_box.text

print(price)

