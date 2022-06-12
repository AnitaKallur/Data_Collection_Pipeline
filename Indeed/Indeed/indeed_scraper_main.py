
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
        # self.driver.implicitly_wait(10)
        # self.uuid4 = uuid.uuid4()
    
        # self.list_of_all_jobs_details = []
        
       
        # while True:   
            
        #     indeed_pagination = self.driver.find_element(by=By.XPATH, value="//span[@class='pn']").click()
            
        #     sleep(3)
        #     pagination_popup = self.driver.find_element(by=By.XPATH, value="//div[@id='popover-x']")
        #     pagination_popup.click()
        #     sleep(3) 
            
        #     indeed_pagination += 1
        #     sleep(2)
        #     if indeed_pagination > 5:
        #         break
        #     else:
        #         break
        
    def scrape(self):
        # self.nevigate_page()
        # self.__get_job_details(self.job_containers)
        global job_indeed
        job_indeed= self.get_job_details(self.job_containers) 
        print(job_indeed)
        # df = pd.DataFrame.from_dict(job_indeed)
        # print(df)
        # return job_indeed    
    
        with open("Data_jobs.json", "w") as outfile:
            json.dump(job_indeed, outfile, indent=4)
    def nevigate_page(self) -> None:
        self.accept_cookies = self.driver.find_element(by=By.XPATH, value= "//button[@id='onetrust-accept-btn-handler']")
        self.accept_cookies.click()
        self.third_element = self.driver.find_element(by=By.XPATH, value= "//div[@class='heading4 color-text-primary singleLineTitle tapItem-gutter']")
        self.third_element.click()
        sleep(3)
        self.fourth_element = self.driver.find_element(by=By.XPATH, value="//td[@class='resultContent']")
    
    # def scrape(self):
        
    #     self.get_job_details(details_container=self.job_containers)
        
    #     sleep(2)
    
    def get_job_details(self, job_containers):
        
        list_of_all_jobs_details = []
        for job_listing in job_containers:
            job_details_dictionary = dict()
            job_details_dictionary["Job Link"] = job_listing.find_element(by=By.XPATH, value=".//a").get_attribute('href')
            job_details_dictionary["Unique ID"] = job_listing.find_element(by=By.XPATH, value=".//a").get_attribute('id')
            job_details_dictionary["Title"] = job_listing.find_element(by=By.XPATH, value=".//h2").text
            job_details_dictionary["Company Name"] = job_listing.find_element(by=By.XPATH, value=".//div/span[@class='companyName']").text
            job_details_dictionary["Company Location"] = job_listing.find_element(by=By.XPATH, value=".//div[@class='companyLocation']").text
            try:
                job_details_dictionary["Salary"] = job_listing.find_element(by=By.XPATH, value= ".//div[@class='metadata salary-snippet-container']").get_attribute('textContent')
            except:
                pass      

            list_of_all_jobs_details.append(job_details_dictionary)
      
        return list_of_all_jobs_details
    
    
    # list_of_jobs = get_job_details(s)
    # print(list_of_jobs)
    
    def download_image(self):
        image_url = ("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=Greater%20London&vjk=f11971796d62ded9")
        image_content = self.driver.get(image_url)
        scraped_images = []
        for image in scraped_images:
            dump_images = image.find_element(by=By.XPATH, value= "//div[@class= 'fe_logo']").get_attribute('img')
            return dump_images
    
    def main(self) -> None:
        
        
        self.scrape()
        print(self.scrape())
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

        