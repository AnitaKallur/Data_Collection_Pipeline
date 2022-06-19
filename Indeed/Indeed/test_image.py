
import sys
import threading

from numpy import product
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json 
import pandas as pd
import numpy as np

from io import StringIO
import pandas as pd
from time import sleep
import requests, openpyxl
import uuid
uuid4 = uuid.uuid4()
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# url = driver.get("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=Greater%20London&vjk=f11971796d62ded9")
# job_containers = driver.find_elements(by=By.XPATH, value="//ul[@class='jobsearch-ResultsList']//div[@class='slider_container css-11g4k3a eu4oa1w0']")
# # self.dataframe = pd.DataFrame(columns=["URL", "ID", "Title", "Company", 
# list_of_all_jobs_details = []


class Scraper:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.url = self.driver.get("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=Greater%20London&vjk=f11971796d62ded9")
        self.job_containers = self.driver.find_elements(by=By.XPATH, value="//ul[@class='jobsearch-ResultsList']//div[@class='slider_container css-11g4k3a eu4oa1w0']")
        # self.dataframe = pd.DataFrame(columns=["URL", "ID", "Title", "Company", "Location", "Salary", "UUID"])
        self.driver.maximize_window()
    def download_image(self):
        # image_url = ("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=Greater%20London&vjk=f11971796d62ded9")
        image_content = self.driver.find_element(by=By.XPATH, value= "//div[@class= 'heading4 color-text-primary singleLineTitle tapItem-gutter'and 'href']")
        image_content.click()
        # for img in image_content:
        #     img_dwd = img.get_attribute("src")
        #     return img_dwd
        # image_content.click()
        image_download = self.driver.find_elements(by=By.XPATH, value="//img")
        for i in image_download:
            images = i.find_elements(by=By.TAG_NAME, value='img')
            for img in images:
                img_src = img.get_attribute("src")
                print (img_src)
        
        # soup = bs(image_content, 'html.parser')
    
        # images = soup.find_all('img')
    
        # for image in images:
        #     name = image['alt']
        #     link = image['src']
        # im = requests.get(link)
        # return name, im
        scraped_images = []
        for image in scraped_images:
            dump_images = image.find_element(by=By.XPATH, value= "//img[@class= 'feLogoImg desktop']").get_attribute('src')
            return dump_images
            
    
    def main(self) -> None:
        
        
        # self.scrape()
        # print(self.scrape())
        self.download_image()
        print(self.download_image())
        # self.scrape()
        # self.get_job_details()
        # self.indeed_full_data()
        # self.get_logo()
       
        self.driver.quit()
if __name__ == "__main__":
    DPS = Scraper()
    DPS.main()
