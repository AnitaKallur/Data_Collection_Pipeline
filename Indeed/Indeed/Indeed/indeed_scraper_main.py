from operator import index
from urllib import response
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys
from numpy import product
import json 
import pandas as pd
import numpy as np
from io import StringIO
import pandas as pd
from time import sleep
import uuid
uuid4 = uuid.uuid4()
import boto3
import plotly
s3_client = boto3.client('s3')
response = s3_client.upload_file('Data_jobs.json', 'databaseindeed', 'jobs_data.json')
s3 = boto3.resource('s3')
my_bucket = s3.Bucket('databaseindeed')
for file in my_bucket.objects.all():
    print(file.key)

""" This class scrapes the website and files the details in a json file"""

class Scraper:
    """Using webdriver to automate the webpage"""
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.url = self.driver.get("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=Greater%20London&vjk=f11971796d62ded9")
        
        
        self.job_containers = self.driver.find_elements(by=By.XPATH, value="//ul[@class='jobsearch-ResultsList']//div[@class='slider_container css-11g4k3a eu4oa1w0']")
        self.driver.maximize_window()
        
        
       
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
        """Assigning a new method to call another method"""
        # self.nevigate_page()
        # self.__get_job_details(self.job_containers)
        global job_indeed
        job_indeed= self.get_job_details(self.job_containers) 
        print(job_indeed)
        # df = pd.DataFrame.from_dict(job_indeed)
        # print(df)
        # return job_indeed    
        """Saving the details in json file"""
        with open("Data_jobs.json", "w") as outfile:
            json.dump(job_indeed, outfile, indent=4)
            
        df = pd.DataFrame.from_dict(job_indeed)
        file_name = r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/Indeed/Indeed'
        print(os.path.isfile(file_name))
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()

            print(lines)
        df.to_csv(r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/Indeed/Indeed', index=index, header=True)
        
    def nevigate_page(self) -> None:
        """ This will accept all cookies """
        # self.close_popup = self.driver.find_element(by=By.XPATH, value="//button[@onclick='closeGoogleOnlyModal()']")
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
        """ Scraping all the details related to the job post"""
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
            # try:
            #     job_details_dictionary["image"] = job_listing.find_element(by=By.XPATH, value= "//a[@class='jcs-JobTitle']").get_attribute('href')  
            # except:
            #     pass
            list_of_all_jobs_details.append(job_details_dictionary)
      
        return list_of_all_jobs_details
    
    
    # list_of_jobs = get_job_details(s)
    # print(list_of_jobs)
    
    def download_image(self):
        """ This will help to download the images/logos from the webpage"""
        # image_url = ("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=Greater%20London&vjk=f11971796d62ded9")
        image_content = self.driver.find_element(by=By.XPATH, value= "//a[@class='jcs-JobTitle']").get_attribute('href')
        
        # image_content.click()
        global image_download
        image_download = self.driver.find_elements(by=By.XPATH, value="//img")
        for i in image_download:
            img_src = i.get_attribute("src")
            return img_src
        print(image_content)
        """Saving the images in json file"""
        with open("Image_jobs.json", "w") as fp:
            json.dump(image_download, fp, indent=4)
        # return image_download
        # try:
        #     # image_content = self.driver.find_elements(by=By.XPATH, value = "//a[@class='jcs-JobTitle']")
        #     # image_content.click()
        #     for img in image_content:
        #         image_download = image_content.find_elements(by=By.XPATH, value="//a[@class='jcs-JobTitle' and '@href']").click()
        #         print(img('href'))
        #         scraped_images.append(img.get_attribute('href'))
        # except Exception as ex:
        #     print(ex)
        # image_download = image_content.find_element(by=By.Xpath, value= "//img").get_attribute('src')
      
        # scraped_images = []
        # for image in scraped_images:
        #     try:
        #         dump_images = self.driver.find_element(by=By.XPATH, value= "//a[@class='jcs-JobTitle']")
        #         for img in dump_images:
        #             self.driver.find_element(by=By.XPATH, value= "//a[@class='jcs-JobTitle']").click()
        #             dump_images= (img('href'))
        #             image.append(dump_images)
        #             return dump_images
        #     except Exception as ex:
        #         print(ex)
                
    
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

        