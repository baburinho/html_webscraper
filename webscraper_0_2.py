# Webscraper 0.0.2
# last edited 6/27/2022 by baburinho

import urllib.request as ul

link = str(input("What website would you like to scrape? ")) # must input full web address (https://www. ; not just www. or the regular domain), need to fix.

def scrape(): # space saving measure for rerun after first
    req = ul.Request(link)
    page = ul.urlopen(req)
    page_data = page.read()
    page.close()

    data = open('webscrape.txt', encoding='utf-8')
    data.write(str(page_data)) #outputs the raw html data into a text file

scrape()

print("All done!")
wish = str(input("Would you like to scrape another website? y/n "))

if wish == 'y':
    link = str(input("What website would you like to scrape? "))
    scrape()
else:
    exit()
