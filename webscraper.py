
# basic webscraper 0.0.1
# purpose is to scrape HTML from webpages and dump into a file on users system
# large parts taken from circuit.rocks' webscraper with modifications to make it a general html scraper instead of merely an intem/price scraper
# last edited by baburinho on 6/26/2022

import urllib.request as ul
from bs4 import BeautifulSoup as soup

url = str(input("Enter URL: ")) 
req = ul.Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # modifies headers of request sent to website; makes bot appear like normal user req
client = ul.urlopen(req) # opening requested URL, reading HTML into variable 'htmldata'
htmldata = client.read()
client.close()

pagesoup = soup(htmldata, "html.parser")
itemlocator = pagesoup.findAll

filename = "scrapedpage.txt"
f = open(filename, "w", encoding="utf-8") #creates file to store scraped HTML; encodes it in unicode to account for non-standard/non-ASCII characters
f.write(str(pagesoup))

# print(pagesoup)
# ^ just to make checking outcomes of modifications easier