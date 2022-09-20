
from posixpath import split
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
from argparse import PARSER
from argparse_prompt import PromptParser
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
        self.driver.maximize_window()
        sleep(1)
  
        
    def nevigate_page(self) -> None:
        """ This will accept all cookies """
        self.accept_cookies = self.driver.find_element(by=By.XPATH, value= "//button[@id='onetrust-accept-btn-handler']")
        self.accept_cookies.click()
        self.fourth_element = self.driver.find_element(by=By.XPATH, value="//td[@class='resultContent']")
        self.driver.find_elements(by=By.XPATH, value="//div[@id='mosaic-provider-jobcards']")
        sleep (2)
        
        for i in range(5):
            
            # df = pd.DataFrame(i)
            
            sleep(1)
            
            details_containers_job_container= self.driver.find_elements(by=By.XPATH, value="//div[@class='slider_item css-kyg8or eu4oa1w0']")
            sleep(3)
            self.new_jobs = self.get_job_details(details_containers_job_container)
            data_scrape = 0
            data_scrape = (self.new_jobs[i])
            
            # data_scrape += 1
            print(len(data_scrape))
            self.df = pd.DataFrame([data_scrape])
            print(self.df)
            # print([data_scrape])
            # print(f' type of the the data is: ' , type(data_scrape))
            sleep(3)
            # print(i)
            # print(f'new job:{new_jobs}')
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3/4);")
            # sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
            
            # df = pd.DataFrame.to_dict(new_jobs)
           
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
            
            try:
                sleep(0.5)
                self.driver.find_element(by=By.XPATH, value="//div[@id='popover-background']").click()
            except:
                # print("This id-label='popupover-x' doesn't exist")
                pass
                
            
            try:
                sleep(0.5)
                self.driver.find_element(by=By.XPATH, value="//a[@data-testid='pagination-page-next']").click()
            except:
                # print("pagination failed")
                pass
            
            save_path = '/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline'
            if not os.path.exists(f'{save_path}/Indeed_jobs_Dataframe'):
                    os.makedirs(f'{save_path}/Indeed_jobs_Dataframe')

            with open(f'{save_path}/Indeed_jobs_Dataframe/Indeed_jobs.json', 'w+') as fp:
                    json.dump(self.new_jobs, fp,  indent=4)
            
            # self.df = pd.DataFrame.from_dict([data_scrape]) 
            # self.df.to_csv(r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/Indeed_jobs_.csv', 
            # index = False, header=True)
            # self.df +=1
    
            if os.path.exists(f'{save_path}/Indeed_jobs_Dataframe/dataframe_Indeed_jobs.csv') and os.path.exists(f'{save_path}/Indeed_jobs_Dataframe/Indeed_jobs.json'):
                self.saving_data = True
                return self.saving_data, save_path

            # print(self.df)
            
        # print(df)
            # print(final_df)
            
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
            
            # print(self.df)
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
        self.get_job_details(details_container)
        
        # print(job_indeed)
        # list_of_jobs = dict()
        # list_of_jobs = self.get_job_details(details_container=self.job_containers)
        # with open("jobs.json", "w") as outfile:
        #     json.dump(job_indeed, outfile, indent=4)
        #     # print(job_indeed)
        # return job_indeed
            # print list_of_jobs
        # save_path = '/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline'
        # if not os.path.exists(f'{save_path}/Indeed_Dataframe'):
        #         os.makedirs(f'{save_path}/Indeed_Dataframe')

        # with open(f'{save_path}/Indeed_Dataframe/Data_jobs.json', 'w+') as fp:
        #     json.dump(job_indeed, fp,  indent=4)
        # global df
        # df = pd.DataFrame.from_dict(job_indeed) 
        # df.to_csv(r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/dataframe_indeed_jobs.csv', 
        # index = False, header=True)
        # # print(df)

        # if os.path.exists(f'{save_path}/Indeed_Dataframe/dataframe_indeed_jobs.csv') and os.path.exists(f'{save_path}/Indeed_Dataframe/Data_jobs.json'):
        #     self.saving_data = True
        #     return self.saving_data, save_path
       
    def connect_to_db(self):
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = 'localhost'
        USER = 'postgres'
        PASSWORD = 'Database123!'
        DATABASE = 'postgres'
        PORT = 5432
        self.engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        self.engine.connect()
        # inspector = inspect(engine)
        # inspector.get_table_names()
        self.engine.execute('''SELECT * FROM dataframe_jobs''').fetchall()
        jobs = pd.read_sql_table('dataframe_jobs', self.engine)
        # print(jobs)
    def aws_upload(self):
        self.df.to_json('/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/Data_jobs.json', orient='records', lines=True )
        
        #send df back to Aws RDS
        self.df.to_sql("dataframe_jobs", self.engine, if_exists="replace")

    
        #upload json S3 bucket     
        # cred = os.getcwd()
        # credentials = pd.read_json(f'{cred}/Indeed/credentials.json', typ='dictionary')
        
        # aws_parser = PromptParser()
        # aws_parser.add_argument('-AU', type=str, help='Please enter your aws_access_key_id', 
        #                     dest='aws_access_key_id',  default = credentials["AWS_ID"])     
        # aws_parser.add_argument('-AP', type = str, help ='Please enter your aws_secret_access_key', 
        #                     dest='aws_secret_access_key', secure=True)
        # aws_parser.add_argument('-BK', type = str, help = 'Please enter AWS S3 BUCKET NAME:', 
        #                     dest='aws_bucket', default=credentials["AWS_BUCKET"])
        # aws_parser.add_argument('-KY',type  = str, help = 'If None, press enter \n Please enter AWS S3 BUCKET KEY(OPTIONAL):',
        #                     dest='aws_key',  default=credentials["AWS_BUCKET_KEY"])
        # self.aws_args = aws_parser.parse_args()

        # self.BUCKET = self.aws_args.aws_bucket
        # self.KEY = self.aws_args.aws_key
        # self.s3 = boto3.client('s3',
        #     aws_access_key_id= self.aws_args.aws_access_key_id,
        #     aws_secret_access_key= self.aws_args.aws_secret_access_key)
        
        
        
        #upload json S3 bucket     
        s3_client = boto3.client('s3')
        response = s3_client.upload_file('Data_jobs.json', 'databaseindeed', 'jobs_data.json')
        s3 = boto3.resource('s3')
        my_bucket = s3.Bucket('databaseindeed')
        for file in my_bucket.objects.all():
            print(file.key)
        # s3 = boto3.client('s3')
        # s3.download_file('Data_jobs.json', 'databaseindeed', 'jobs_data.json')
        
        # s3_name=str('data_jobs.json')
        # s3_client =boto3.client('s3')
        # s3_client.upload_file('/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/data_jobs.json', 'dataframe_jobs', s3_name)
                   
        #remove json files from the system
        os.remove('/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/Data_jobs.json')
        self.df.to_json 
        
        # s3_client = boto3.client('s3')
        # response = s3_client.upload_file('Data_jobs.json', 'databaseindeed', 'jobs_data.json')
        # s3 = boto3.resource('s3')
        # my_bucket = s3.Bucket('databaseindeed')
        # for file in my_bucket.objects.all():
        #     print(file.key)
        
        
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
            # df = pd.DataFrame(list_of_all_jobs_details)
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
       

    def main_jobs(self) -> None:
        self.nevigate_page()
        self.page_scroll()
        self.download_image()
        self.connect_to_db()
        self.aws_upload()
        self.driver.quit()
        
if __name__ == "__main__":
    DPS = Scraper()
    DPS.main_jobs()

        