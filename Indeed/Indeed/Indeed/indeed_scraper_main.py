

from matplotlib.pyplot import axis
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
from tabulate import tabulate
import requests, openpyxl
import csv
import os
import sys
from numpy import product
import numpy as np
from psycopg2.extensions import register_adapter, AsIs
import json 
import psycopg2
import postgres
import pandas as pd
import io
from io import StringIO
from pandas import DataFrame
from time import sleep
import uuid
from io import StringIO

from yaml import warnings
uuid4 = uuid.uuid4()
import boto3
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

details_container = []

""" This class scrapes the website and files the details in a json file"""

class Scraper:
    """Using webdriver to automate the webpage"""
    def __init__(self) -> None:
        options = FirefoxOptions()
        options.headless = True
        # self.opt.add_argument("--headless")
        # self.driver = webdriver.Chrome(service= Service(ChromeDriverManager().install())
        
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        self.url = self.driver.get("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=London%2C%20Greater%20London&vjk=f11971796d62ded9")
        self.driver.maximize_window()
        sleep(1)
  
        
    def navigate_page(self) -> None:
        """ This will accept all cookies """
        self.accept_cookies = self.driver.find_element(by=By.XPATH, value= "//button[@id='onetrust-accept-btn-handler']")
        self.accept_cookies.click()
        self.fourth_element = self.driver.find_element(by=By.XPATH, value="//td[@class='resultContent']")
        self.driver.find_elements(by=By.XPATH, value="//div[@id='mosaic-provider-jobcards']")
        sleep (2)
        self.data_scrape = []
        for i in range(25):
            
            # df = pd.DataFrame(i)
            # data_scrape = dict()
            sleep(3)
            
            details_containers_job_container= self.driver.find_elements(by=By.XPATH, value="//div[@class='slider_item css-kyg8or eu4oa1w0']")
            sleep(3)
            
            self.new_jobs = self.get_job_details(details_containers_job_container) 
             
            
            # print(self.data_scrape)
            i+=1
            sleep(3)
            self.data_scrape.append(self.new_jobs)  
            
            
            
            self.columns = ['Job_Link','Unique_ID', 'Title', 'Company_Name', 'Company_Location', 'Salary']
            self.data_scrape.append(self.df)
            self.data_scrape = [self.job_link,self.unique_id, self.title,  self.company_name,  self.company_location,  self.salary]
            pages = 3
            self.df_1 = pd.DataFrame(self.data_scrape, index=None)
            # self.df_1.transpose()
            # self.df_2 = pd.concat(self.df, self.df_1)
            
            self.df_1 =self.df_1.transpose()
            self.df_1.columns = self.columns
            
            # page+=1
            
            
            
            print(self.df_1)
            sleep(3)
            if os.path.exists('Indeed_data_nw.csv'):
                self.df_1.to_csv('Indeed_data_new.csv',mode='a',header=True, index=False)
            else:
                self.df_1.to_csv('Indeed_data_new.csv', mode='a',header=True, index=False)
            # print(self.data_scrape)
            # print(self.data_scrape)
            # self.data_scrape.append(self.df)
            # self.df_1 - pd.DataFrame(self.data_scrape)
            # self.data_scrape = list(self.df.values())
            # print(self.data_scrape)
            # self.data_scrape = zip(self.new_jobs.keys(), self.new_jobs.values())
            # self.data_scrape = list(self.data_scrape)
            # self.df_1 = self.data_scrape.append(self.df)
            # print(self.df_1)
            # self.df_1 = self.df_1.to_csv("datascrape_new.csv", index=False, na_rep ='None', quoting = False, index_label=None, line_terminator='\n',quotechar=' ')
            # print(self.df_1)
            # self.df_1 = self.df_1.transpose()
            # print(self.df_1)
            # print(type(self.df_1))
            # print(self.df_1)
            # for key, val in self.df.items():
            #     self.data_scrape.append([key,val])
            #     print(self.data_scrape)
            # self.data_scrape = ({'Job_Link':self.job_link,'Unique_ID': self.unique_id, 'Title': self.title, 'Company_Name': self.company_name, 'Company_Location': self.company_location, 'Salary': self.salary})
            # self.columns=['Job_Link','Unique_ID', 'Title', 'Company_Name', 'Company_Location', 'Salary']
            # self.df_1 = pd.DataFrame(self.data_scrape, index=None, columns=self.columns)
            # print(self.df_1)
            # print(len(self.df_1.columns))
            # self.data_f = pd.DataFrame([self.data_scrape])
            # print(len(self.df.columns))
            # print(self.data_scrape)
            # # self.df.loc[len(self.df)]= self.data_scrape
            # print(self.df2)
            
           
            # print(len(self.data_f.columns))
            # self.data_f.columns = ['Job_Link','Unique_ID', 'Title', 'Company_Name', 'Company_Location', 'Salary']
            # # print(self.data_f)
            # print(self.data_f)
            # df = pd.read_csv(io.StringIO(self.data_f), delim_whitespace=True, header=None, names=['Job_Link','Unique_ID', 'Title', 'Company_Name', 'Company_Location', 'Salary'])
            # print(df)
            # self.df_1.to_csv("data.csv", index=False, na_rep ='None', quoting = False, index_label=None, line_terminator='\n',quotechar=' ')
            # print(self.data_scrape)
            
            sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)
           
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
    def data_store(self):
        dfs = []
        save_path = '/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline'
        if not os.path.exists(f'{save_path}/Indeed_jobs_Dataframe'):
                os.makedirs(f'{save_path}/Indeed_jobs_Dataframe')

        with open(f'{save_path}/Indeed_jobs_Dataframe/data_jobs_new.json', 'w+') as fp:
                json.dump(self.new_jobs, fp,  indent=4)
        # column_names = ['Job_Link' ,'Unique_ID','Title','Company_Name','Company_Location','Salary']
        # with open(self.data_f, 'r', newline='') as f:
        #     reader = csv.reader(f)
        #     # Skip header row
        #     next(reader)
        # self.data_f.to_csv(r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/data_jobs_new.csv', 
        # index=False, quoting = False, index_label=None, header = None,line_terminator='\n', quotechar=' ')
        # # self.data_f.to_excel(r'/Users/prabhuswamikallur/Desktop/data_jobs_new.xlsx', index= None, header=True )
        # # self.df +=1

        if os.path.exists(f'{save_path}/Indeed_jobs_Dataframe/data_jobs_new.csv') and os.path.exists(f'{save_path}/Indeed_jobs_Dataframe/Indeed_jobs.json'):
            self.saving_data = True
            return self.saving_data, save_path
            
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
            # print(f"scrolled {i} time(s)")
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
              
    def connect_to_db(self):
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = 'localhost'
        USER = 'postgres'
        PASSWORD = 'postgres'
        DATABASE = 'job_indeed'
        PORT = 5432
        
        # self.engine =pymysql.connect(
        # HOST=HOST,
        # USER=USER,
        # PASSWORD=PASSWORD,
        # DATABASE=DATABASE,
        # autocommit=True)
        self.engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        self.engine.connect()
        # inspector = inspect(engine)
        # inspector.get_table_names()
        self.engine.execute('''SELECT * FROM indeed_jobs''').fetchall()
        jobs = pd.read_sql_table('indeed_jobs', self.engine)
        print(jobs)
    def aws_upload(self):
        self.df_1.to_json('/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/Data_jobs.json', orient='records', lines=True )
        
        #send df back to Aws RDS
        self.df_1.to_sql("indeed_jobs", self.engine, if_exists="replace")

    
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
            return file.key
        
        s3 = boto3.client('s3')
        s3.download_file('databaseindeed', )
            # print(file.key)
        # s3 = boto3.client('s3')
        # s3.download_file('Data_jobs.json', 'databaseindeed', 'jobs_data.json')
        
        # s3_name=str('data_jobs.json')
        # s3_client =boto3.client('s3')
        # s3_client.upload_file('/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/data_jobs.json', 'dataframe_jobs', s3_name)
                   
        #remove json files from the system
        os.remove('/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/Data_jobs.json')
        self.df_1.to_json 
        
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
        self.job_link =[]
        self.unique_id = []
        self.title = []
        self.company_name =[]
        self.company_location =[]
        self.salary = []
        for job_listing in details_container:
            # global job_details_dictionary
            job_details_dictionary = dict()
            try:
                job_links = job_listing.find_element(by=By.XPATH, value=".//a").get_attribute('href')
                self.job_link.append(job_links)
            except NoSuchElementException:
                self.job_link.append('NaN')
                
            try:
                job_id = job_listing.find_element(by=By.XPATH, value=".//a").get_attribute('id')
                self.unique_id.append(job_id)
            except NoSuchElementException:
                self.unique_id.append('NaN')
            # job_details_dictionary["Title"] = job_listing.find_element(by=By.XPATH, value=".//h2").text
            try:
                job_titile = job_listing.find_element(by=By.XPATH, value="//a[@class='jcs-JobTitle css-jspxzf eu4oa1w0']").text
                self.title.append(job_titile)
            except NoSuchElementException:
                self.title.append('NaN')
            try:
                job_company = job_listing.find_element(by=By.XPATH, value=".//div/span[@class='companyName']").text
                self.company_name.append(job_company)
            except NoSuchElementException:
                self.company_name.append('NaN')
            try:
                job_location = job_listing.find_element(by=By.XPATH, value=".//div[@class='companyLocation']").text
                self.company_location.append(job_location)
            except NoSuchElementException:
                self.company_location.append('NaN')
            try:
                job_salary = job_listing.find_element(by=By.XPATH, value= ".//div[@class='metadata salary-snippet-container']").get_attribute('textContent')
                self.salary.append(job_salary)
            except NoSuchElementException:
                self.salary.append('NaN')
  
            self.df =pd.DataFrame ({'Job_Link':self.job_link,'Unique_ID': self.unique_id, 'Title': self.title, 'Company_Name': self.company_name, 'Company_Location': self.company_location, 'Salary': self.salary})
           
    def download_image(self):
        """ This will help to download the images/logos from the webpage"""
       
        images = []
        image_container = self.driver.find_elements(by=By.XPATH, value="//img")
        for img in image_container:
            img_src =self.driver.find_element(by=By.XPATH, value="//img").get_attribute("src")
            images.append(img_src)
            
        for i in range(len(images)):
            if i >10:
                break
            response = requests.get(images[i])
            file = open(r"/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/logo.jpg"+str(i)+".jpg", "wb")  
            file.write(response.content)  
            
        # """Saving the images in json file"""
        # with open("Image_jobs.json", "w") as fp:
        #     json.dump(images, fp, indent=4)
       

            
    def scraper_main(self) -> None:
        self.navigate_page()
        self.page_scroll()
        self.data_store()
        self.download_image()
        self.connect_to_db()
        self.aws_upload()
        self.driver.quit()
        
if __name__ == "__main__":
    DPS = Scraper()
    DPS.scraper_main()

        