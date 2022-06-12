from operator import index
from typing import Any
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json
import selenium
from numpy import product
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
from time import sleep
from io import StringIO
import io
import pandas as pd

# from Indeed.Indeed.test import download_image
# driver = webdriver.Chrome()
class Scraper:
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.get("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=Greater%20London&vjk=f11971796d62ded9")
    # job_containers = driver.find_elements(by=By.XPATH, value="//ul[@class='jobsearch-ResultsList']//div[@class='slider_container css-11g4k3a eu4oa1w0']")

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.url = self.driver.get("https://uk.indeed.com/jobs?q=Data%20Engineer%20or%20Data%20Scientist%20&l=London&start=10&vjk=b743fcd24895ddba")
        self.job_containers = self.driver.find_elements(by=By.XPATH, value="//ul[@class='jobsearch-ResultsList']//div[@class='slider_container css-11g4k3a eu4oa1w0']")
        self. image_url = "https://uk.indeed.com/jobs?q=Data%20Engineer%20or%20Data%20Scientist%20&l=London%2C%20Greater%20London&vjk=63c92ffb71fad229&advn=9660210449134183"
        self.driver.maximize_window()
    def scrape(self):
        # self.nevigate_page()
        # self.__get_job_details(self.job_containers)
        job_indeed= self.__get_job_details(self.job_containers) 
        return job_indeed
    
    def nevigate_page(self) -> None:
        # Accept cookies
        self.accept_cookies = self.driver.find_element(by=By.XPATH, value= "//button[@id='onetrust-accept-btn-handler']")
        self.accept_cookies.click()
        # self.third_element = self.driver.find_element(by=By.XPATH, value= "//div[@class='heading4 color-text-primary singleLineTitle tapItem-gutter']")
        # self.third_element.click()
        # sleep(3)
        self.fourth_element = self.driver.find_element(by=By.XPATH, value="//td[@class='resultContent']")

    # def __iter__(self):
    # #     # self.job_containers = self.driver.find_elements(by=By.XPATH, value="//ul[@class='jobsearch-ResultsList']//div[@class='slider_container css-11g4k3a eu4oa1w0']")
    #     yield self

    def __get_job_details(self, job_containers):
    # self.job_containers = self.driver.find_elements(by=By.XPATH, value="//ul[@class='jobsearch-ResultsList']//div[@class='slider_container css-11g4k3a eu4oa1w0']")
        list_of_all_jobs_details = []
    
        for job_listing in job_containers:
            job_details_dictionary = dict()
            job_details_dictionary["Job Link"] = job_listing.find_element(by=By.XPATH, value=".//a").get_property('href')
            
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
    
        
    # list_of_jobs = __get_job_details(self.job_containers)
    # print(list_of_jobs)
    # with open("jobs.json", "w") as outfile:
    #     json.dump(list_of_jobs, outfile, indent=4)
    
    def download_image(self):
       
        image_content = requests.get(self.url).content
    
    
        soup = BeautifulSoup(image_content, 'html.parser')
    
        images = soup.find_all('img')
    
        for image in images:
            name = image['alt']
            link = image['src']
        ret
        
        with open ("json_image", "w") as f:
                    im = requests.get(link)
                    f.dump(im.content, image_file, f, index = 4)
                    # print('Writing: ', name)
        
            
        # image = image.open(image_content)
        # file_path = download_path + file_name
        # with open(file_path, "wb") as f:
        #     image.save(f, "JPEG")
        # return image
    
        # self.__get_job_details(details_container=self.job_containers)   
    def main(self) -> None:
        self.scrape()
        print(self.scrape())
        self.download_image()
        print(self.download_image())
        # print(job_indeed)
        # self.nevigate_page()
        # self.__iter__()
        # self.__get_job_details()
        # self.indeed_full_data()
        # self.get_logo()
    
        self.driver.quit()
if __name__ == "__main__":
    DPS = Scraper()
    DPS.main()