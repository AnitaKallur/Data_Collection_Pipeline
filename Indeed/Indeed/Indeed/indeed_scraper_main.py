
from matplotlib.pyplot import axis
import requests
from selenium import webdriver 
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
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

details_container = []

""" This class scrapes the website and files the details in a json file"""

class Scraper:
    """Using webdriver to automate the webpage"""
    def __init__(self) -> None:
        options = FirefoxOptions()
        # options.headless = True
        # self.opt.add_argument("--headless")
        # self.driver = webdriver.Chrome(service= Service(ChromeDriverManager().install())
        
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        self.url = self.driver.get("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=London%2C%20Greater%20London&vjk=f11971796d62ded9")
        # self.url_bs = ("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=London%2C%20Greater%20London&vjk=f11971796d62ded9")
        # self.details_containers_job_container = self.driver.find_elements(by=By.XPATH, value="//ul[@class='jobsearch-ResultsList']//div[@class='slider_container css-11g4k3a eu4oa1w0']")
        # sleep(2)
        # self.driver.set_window_size(800, 600)
        self.driver.maximize_window()
        sleep(1)
  
        
    def nevigate_page(self) -> None:
        """ This will accept all cookies """
        # self.close_popup = self.driver.find_element(by=By.XPATH, value="//button[@onclick='closeGoogleOnlyModal()']")
        self.accept_cookies = self.driver.find_element(by=By.XPATH, value= "//button[@id='onetrust-accept-btn-handler']")
        self.accept_cookies.click()
        # self.third_element = self.driver.find_element(by=By.XPATH, value= "//div[@class='heading4 color-text-primary singleLineTitle tapItem-gutter']")
        # self.third_element.click()
        # sleep(1)
        self.fourth_element = self.driver.find_element(by=By.XPATH, value="//td[@class='resultContent']")
        self.driver.find_elements(by=By.XPATH, value="//div[@id='mosaic-provider-jobcards']")
        sleep (2)
        # delay = sleep(10)
        # details_containers_job_container = self.driver.find_elements(by=By.XPATH, value="//div[@class='mosaic mosaic-provider-jobcards mosaic-provider-hydrated']")
        for i in range(10):
            
            sleep(1)
            
            details_containers_job_container= self.driver.find_elements(by=By.XPATH, value="//div[@class='slider_item css-kyg8or eu4oa1w0']")
            sleep(3)
            new_jobs = self.get_job_details(details_containers_job_container)
            sleep(3)
            # print(f'new job:{new_jobs}')
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3/4);")
            # sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
            try:
                sleep(0.5)
                self.driver.find_element(by=By.XPATH, value="//a[@data-testid='pagination-page-next']").click()
            except:
                # print("pagination failed")
                pass
            
            try:
                sleep(0.5)
                self.driver.find_element(by=By.XPATH, value="//a[@aria-label='Next']").click()
            except:
                # print("This aria-label='Next' doesn't exist")
                pass

            try:
                sleep(0.5)
                self.driver.find_element(by=By.XPATH, value="//button[@class='icl-CloseButton icl-Card-close']").click()
            except:
                # print("This id-label='popupover-x' doesn't exist")
                pass

            try:
                sleep(0.5)
                self.driver.find_element(by=By.XPATH, value="//div[@id='popover-x']").click()
            except:
                # print("This id-label='popupover-x' doesn't exist")
                pass
                
            try:
                sleep(0.5)
                self.driver.find_element(by=By.XPATH, value="//div[@id='popover-x']").click()
            except:
                # print("This id-label='popupover-x' doesn't exist")
                pass
                
                
            save_path = '/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline'
            if not os.path.exists(f'{save_path}/New_Indeed_Dataframe'):
                    os.makedirs(f'{save_path}/New_Indeed_Dataframe')

            with open(f'{save_path}/New_Indeed_Dataframe/New_jobs.json', 'w+') as fp:
                json.dump(new_jobs, fp,  indent=4)
            # global df
            df = pd.DataFrame.from_dict(new_jobs) 
            df.to_csv(r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/New_dataframe_indeed_jobs.csv', 
            index = False, header=True)
        

            if os.path.exists(f'{save_path}/Indeed_Dataframe/dataframe_indeed_jobs.csv') and os.path.exists(f'{save_path}/Indeed_Dataframe/Data_jobs.json'):
                self.saving_data = True
                return self.saving_data, save_path
            print(new_jobs)
            print(df)
            
    def page_scroll(self) -> None:
        self.scrape()
        self.last_height = self.driver.execute_script('return document.body.scrollHeight')
        # sleep(3)
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # sleep(3)
        #new_height = driver.execute_script('return document.body.scrollHeight')
        #sleep(3)
        self.scroll_pause_time = 3
        i = 0
        self.number_of_scrolls = 3
        while i < self.number_of_scrolls:
            print(f"scrolled {i} time(s)")
            sleep(1)
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(1)
            sleep(self.number_of_scrolls)
            
            self.new_height = self.driver.execute_script(
                        "return document.body.scrollHeight")
            if self.new_height == self.last_height:
                break
            i += 1
            self.last_height = self.new_height
        
        
    def scrape(self):
        """Assigning a new method to call another method"""
        # self.nevigate_page()
        # self.__get__job_details(self.job_containers)
        job_indeed= self.get_job_details(details_container)
        # print(job_indeed)
        # list_of_jobs = dict()
        # list_of_jobs = self.get_job_details(details_container=self.job_containers)
        # with open("jobs.json", "w") as outfile:
        #     json.dump(job_indeed, outfile, indent=4)
        #     # print(job_indeed)
        # return job_indeed
            # print list_of_jobs
        save_path = '/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline'
        if not os.path.exists(f'{save_path}/Indeed_Dataframe'):
                os.makedirs(f'{save_path}/Indeed_Dataframe')

        with open(f'{save_path}/Indeed_Dataframe/Data_jobs.json', 'w+') as fp:
            json.dump(job_indeed, fp,  indent=4)
        global df
        df = pd.DataFrame.from_dict(job_indeed) 
        df.to_csv(r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/dataframe_indeed_jobs.csv', 
        index = False, header=True)
        print(df)

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
        # os.remove('/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/Data_jobs.json')
        # df.to_json
        
        
        
       
    
    # def scrape(self):
        
    #     self.get_job_details(details_container=self.job_containers)
        
    #     sleep(2)
    
    def get_job_details(self, details_container):
        """ Scraping all the details related to the job post"""
        # global details_container
        # self.details_container = details_container
        # global details_container
        
        list_of_all_jobs_details = []
        # details_container = []
        # global details_container
        new_unique_id = [] 
        # while True:
        
        for job_listing in details_container:
            # global job_details_dictionary
            job_details_dictionary = dict()
            
            job_details_dictionary["Job_Link"] = job_listing.find_element(by=By.XPATH, value=".//a").get_attribute('href')
            job_details_dictionary["Unique_ID"] = job_listing.find_element(by=By.XPATH, value=".//a").get_attribute('id')
            # job_details_dictionary["Title"] = job_listing.find_element(by=By.XPATH, value=".//h2").text
            job_details_dictionary["Title"] = job_listing.find_element(by=By.XPATH, value="//a[@class='jcs-JobTitle css-jspxzf eu4oa1w0']").text
            job_details_dictionary["Company_Name"] = job_listing.find_element(by=By.XPATH, value=".//div/span[@class='companyName']").text
            job_details_dictionary["Company_Location"] = job_listing.find_element(by=By.XPATH, value=".//div[@class='companyLocation']").text
            try:
                job_details_dictionary["Salary"] = job_listing.find_element(by=By.XPATH, value= ".//div[@class='metadata salary-snippet-container']").get_attribute('textContent')
            except:
                pass   
            # break
            # try:
            #     job_details_dictionary["image"] = job_listing.find_element(by=By.XPATH, value= "//a[@class='jcs-JobTitle']").get_attribute('href')  
            # except:
            #     pass
            
            # if new_unique_id not in job_details_dictionary["Unique_ID"]:
            #     list_of_all_jobs_details.append(new_unique_id)
            # else:
            #     print("Item already in the list")
    
            list_of_all_jobs_details.append(job_details_dictionary)
            # print(list_of_all_jobs_details)
            
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
       
   
    
    def main(self) -> None:
        self.nevigate_page()
       
        self.page_scroll()
        # self.get_job_details(details_container=)
        # self.scrape()
        # print(self.scrape())
        # self.get_dataframe()
       
       
        self.driver.quit()
if __name__ == "__main__":
    DPS = Scraper()
    DPS.main()

        