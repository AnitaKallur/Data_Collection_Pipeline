
from numpy import product
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re
import urllib.request
import lxml.html
import wget
import requests, openpyxl
import urllib.request
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title ='Top rated TVshows'
print(excel.sheetnames)
sheet.append(['Show Rank', 'Show Name', 'Year of Release', 'IMBD Rating'])
import re
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
from time import sleep
from settings import URL

import uuid
uuid4 = uuid.uuid4()
class scraper:
        def __init__(self) -> None:
                self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                self.url = self.driver.get(URL)
                self.soup =bs(self.driver.page_source, "html.parser")
                #self.driver.implicitly_wait(10)
                #self.url = URL
                #self.response = requests.get(self.url)
                #self.soup = BeautifulSoup(self.response.text, "html.parser")
                #print(soup)
                
        def nevigate_page(self):
                parent = self.soup.find('td', class_= 'titleColumn')
                child = parent.find('a')['href']
                print(child)
                        
                      
                
                """ sheet.append([self.rank, self.name, self.year, self.rating])
                excel.save('IMBD TVshow Ratings.xlsx') """
                        
        def get_details(self):
                self.tv_shows = self.soup.find('tbody', class_='lister-list').find_all('tr')
                for show in self.tv_shows:
                        self.name = show.find('td', class_='titleColumn').a.text
                        #self.link = show.find('td', 'href a') 
                        self.rank = show.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
                        self.year = show.find('td', class_='titleColumn').span.text.strip('()')
                        self.rating = show.find('td', class_='ratingColumn imdbRating').strong.text
                        self.link = show.find('td')
                        print(self.rank, self.name, self.year, self.rating)
                        sheet.append([self.rank, self.name, self.year, self.rating])
                excel.save('IMBD TVshow Ratings.xlsx')
        def main(self) -> None:
                self.nevigate_page()
                #self.get_details()
                #self.page_scroll()
                            
if __name__ == "__main__":
    DPS = scraper()
    DPS.main()

        