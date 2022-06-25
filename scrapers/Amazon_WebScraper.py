# import library

from cgitb import text
from re import A
import requests
from bs4 import BeautifulSoup
import time
import datetime
import smtplib
url = 'https://www.amazon.co.uk/Best-Sellers-Electronics-Photo/zgbs/electronics'
headers = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
#def extract_data(url):
#url = 'https://www.amazon.co.uk/Best-Sellers-Electronics-Photo/zgbs/electronics/ref=zg_bs_nav_0'
#headers = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')
page = soup.find_all('li', 'a')
print(soup.prettify)

    

""" def navigate_page(soup):
    global page
    page = soup.find('ul', {'class': 'a-pagination"'})
    if not page.find('li', {'class': 'a-disabled a-last'}):
        url = 'https://www.amazon.co.uk' + str ( page.find('li', {'class': 'a-last'})).find('a')['href']
        return url
    else:
        return
    
extract_data(url) """