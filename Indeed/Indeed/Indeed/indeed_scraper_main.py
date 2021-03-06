from operator import index
from ssl import Options
from urllib import response
from cv2 import sepFilter2D
from matplotlib.pyplot import axis
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
import sys
from numpy import product
import json 
import psycopg2 as ps
import sqlalchemy
import postgres
import pandas as pd
import numpy as np
from io import StringIO
import pandas as pd
from pandas import DataFrame
from time import sleep
import uuid
uuid4 = uuid.uuid4()
import boto3
import plotly
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect



""" This class scrapes the website and files the details in a json file"""

class Scraper:
    """Using webdriver to automate the webpage"""
    def __init__(self) -> None:
        self.opt = Options()
        self.opt.add_argument("--headless")
        # self.driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=self.opt )
        self.url = self.driver.get("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=Greater%20London&vjk=f11971796d62ded9")
        self.url_bs = ("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=Greater%20London&vjk=f11971796d62ded9")
        
        
        
        self.job_containers = self.driver.find_elements(by=By.XPATH, value="//ul[@class='jobsearch-ResultsList']//div[@class='slider_container css-11g4k3a eu4oa1w0']")
        self.driver.maximize_window()
        
        # pagination = self.driver.find_element(by=By.XPATH, value = "//a[@aria-label='2']")
        # pagination.click()
    
        
        
    # def get_record(self): 
            
    #     while True:   
    #         try:
    #             self.pagination = self.soup.find('a', {'aria-label': 'Next'}).get('href')
    #         except AttributeError:
    #             break
    #         self.response = requests.get(self.pagination)
    #         self.soup = bs(self.response.text, "html.parser")
    #         self.response = requests.get(self.url_bs)
    #         cards = self.soup.find_all('div', 'jobsearch-SerpJobCard')
    #         records = []
    #         for card in cards:
    #             self.record = self.get_record(card)
    #         records.append(self.record)
    #         print(len(records))
            # indeed_pagination = self.driver.find_element(by=By.XPATH, value="//a[@aria-label='Next']").get_attribute('href')
            # indeed_pagination.c
            # sleep(3)
            # pagination_popup = self.driver.find_element(by=By.XPATH, value="//div[@id='popover-x']")
            # pagination_popup.click()
            # sleep(3) 
            
            # self_pagination += 1
            # sleep(2)
            # if indeed_pagination > 3:
            #     break
            # else:
            #     break
        
    def scrape(self):
        """Assigning a new method to call another method"""
        # self.nevigate_page()
        # self.__get_job_details(self.job_containers)
        job_indeed= self.get_job_details(self.job_containers)
        save_path = '/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline'
        if not os.path.exists(f'{save_path}/Indeed_Dataframe'):
                os.makedirs(f'{save_path}/Indeed_Dataframe')

        with open(f'{save_path}/Indeed_Dataframe/Data_jobs.json', 'w+') as fp:
            json.dump(job_indeed, fp,  indent=4)
        global df
        df = pd.DataFrame.from_dict(job_indeed) 
        df.to_csv(r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/dataframe_indeed_jobs.csv', 
        index = False, header=True)
        

        if os.path.exists(f'{save_path}/Indeed_Dataframe/dataframe_indeed_jobs.csv') and os.path.exists(f'{save_path}/Indeed_Dataframe/Data_jobs.json'):
            self.saving_data = True
            return self.saving_data, save_path
       
    def connect_to_db(self):
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = 'localhost'
        USER = 'postgres'
        PASSWORD = 'Database123!'
        DATABASE = 'postgres'
        PORT = 5432
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        engine.connect()
        # inspector = inspect(engine)
        # inspector.get_table_names()
        engine.execute('''SELECT * FROM dataframe_jobs''').fetchall()
        jobs = pd.read_sql_table('dataframe_jobs', engine)
        # print(jobs)
    # def aws_upload(self, df):
        df.to_json('/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/Data_jobs.json', orient='records', lines=True )
        
        #send df back to Aws RDS
        df.to_sql("dataframe_jobs", engine, if_exists="replace")

    
        #upload json S3 bucket     
        s3_client = boto3.client('s3')
        response = s3_client.upload_file('Data_jobs.json', 'databaseindeed', 'jobs_data.json')
        s3 = boto3.resource('s3')
        my_bucket = s3.Bucket('databaseindeed')
        for file in my_bucket.objects.all():
            print(file.key)
        
        
        # s3_name=str('data_jobs.json')
        # s3_client =boto3.client('s3')
        # s3_client.upload_file('/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/data_jobs.json', 'dataframe_jobs', s3_name)
                   
        #remove json files from the system
        os.remove('/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/Data_jobs.json')
        df.to_json
        
        
        
       
    def nevigate_page(self) -> None:
        """ This will accept all cookies """
        # self.close_popup = self.driver.find_element(by=By.XPATH, value="//button[@onclick='closeGoogleOnlyModal()']")
        self.accept_cookies = self.driver.find_element(by=By.XPATH, value= "//button[@id='onetrust-accept-btn-handler']")
        self.accept_cookies.click()
        # self.third_element = self.driver.find_element(by=By.XPATH, value= "//div[@class='heading4 color-text-primary singleLineTitle tapItem-gutter']")
        # self.third_element.click()
        sleep(3)
        self.fourth_element = self.driver.find_element(by=By.XPATH, value="//td[@class='resultContent']")
    
    # def scrape(self):
        
    #     self.get_job_details(details_container=self.job_containers)
        
    #     sleep(2)
    
    def get_job_details(self, job_containers):
        """ Scraping all the details related to the job post"""
        list_of_all_jobs_details = []
        new_unique_id = []
        for job_listing in job_containers:
            global job_details_dictionary
            job_details_dictionary = dict()
            job_details_dictionary["Job_Link"] = job_listing.find_element(by=By.XPATH, value=".//a").get_attribute('href')
            job_details_dictionary["Unique_ID"] = job_listing.find_element(by=By.XPATH, value=".//a").get_attribute('id')
            job_details_dictionary["Title"] = job_listing.find_element(by=By.XPATH, value=".//h2").text
            job_details_dictionary["Company_Name"] = job_listing.find_element(by=By.XPATH, value=".//div/span[@class='companyName']").text
            job_details_dictionary["Company_Location"] = job_listing.find_element(by=By.XPATH, value=".//div[@class='companyLocation']").text
            try:
                job_details_dictionary["Salary"] = job_listing.find_element(by=By.XPATH, value= ".//div[@class='metadata salary-snippet-container']").get_attribute('textContent')
            except:
                pass   
            # try:
            #     job_details_dictionary["image"] = job_listing.find_element(by=By.XPATH, value= "//a[@class='jcs-JobTitle']").get_attribute('href')  
            # except:
            #     pass
            
            if new_unique_id not in job_details_dictionary["Unique_ID"]:
                list_of_all_jobs_details.append(new_unique_id)
            else:
                print("Item already in the list")
    
            list_of_all_jobs_details.append(job_details_dictionary)
            print(list_of_all_jobs_details)
        return list_of_all_jobs_details
        
 
    def download_image(self):
        """ This will help to download the images/logos from the webpage"""
        # image_url = ("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=Greater%20London&vjk=f11971796d62ded9")
        # image_content = self.driver.find_element(by=By.XPATH, value= "//a[@class='jcs-JobTitle']").get_attribute('href')
        
        # image_content.click()
        global image_download
        image_download = self.driver.find_elements(by=By.XPATH, value="//img")
        for i in image_download:
            img_src = i.get_attribute("src")
            return img_src
        # print(image_content)
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
        
        # self.get_record()
        self.scrape()
        print(self.scrape())
        self.download_image()
        print(self.download_image())
        # self.get_dataframe()
        # print(self.get_dataframe)
        self.connect_to_db()
        
        # self.scrape()
        # self.get_job_details()
        # self.indeed_full_data()
        # self.get_logo()
       
        self.driver.quit()
if __name__ == "__main__":
    DPS = Scraper()
    DPS.main()

        