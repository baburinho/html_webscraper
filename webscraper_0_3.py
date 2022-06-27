# webscraper 0.0.3
# last edited 6/27 by baburinho
# parsable html edition :)
# if you pay attention you can figure out which tutorial i grabbed a lot of this stuff from lol

import urllib.request as ul
from bs4 import BeautifulSoup as bsoup
import string

def scrape(): # space saving measure for rerun after first
    link = str(input('What website would you like to scrape? '))
    req = ul.Request(link)

    page = ul.urlopen(req)
    page_data = page.read()
    page.close()
    
    html = open('page_html.html', 'w+', encoding='utf-8')
    html.write(str(page_data))

    html_soup = open('page_html.html', 'r+')

    soup = bsoup(html_soup, 'html.parser')
    what_data = input('What data would you like to be scraped from this site? All or just text?')

    if what_data == "all" or "All" or "ALL":
        file = open("page_data.txt", 'w+' , encoding='utf-8')
        file.write(str(page_data))
    elif what_data == 'text' or 'Text' or 'just text' or 'Just text':
        txt = string.printable()
        page_text = soup.find(txt)
        actual_text = page_text.find_all(page_text=True)
        file = open("page_data.txt", encoding='utf-8')
        file.write(str(actual_text))


scrape()

print("\nAll done!")

wish = input("\nWould you like to scrape another site? y/n ")

if wish == 'y':
    scrape()
    print("\nAll done! Have a nice day!")
else:
    print('\nAlright! Have a nice day!')
    exit()