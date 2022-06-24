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
        job_indeed = dict()
        job_indeed= self.get_job_details(self.job_containers) 
        # print(job_indeed)
        # df = pd.DataFrame.from_dict(job_indeed)
        # df.to_csv = ('df.csv')
        # df.to_csv= (r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/df.csv')
        # print(df)
        # print(df)
        
        # return job_indeed    
        """Saving the details in json file"""
        with open("Data_jobs.json", "w") as outfile:
            json.dump(job_indeed, outfile, indent=4)
    # global jobs_dataframe
    
    
    def get_dataframe(self):
        self.job_data = jobs_dataframe
        df = pd.DataFrame.from_dict(job_indeed)
        df=df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df.to_csv = ('dataframe_indeed.csv')
        df.to_csv= (r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/dataframe_indeed.csv')
        print(df)
        # df = pd.DataFrame.from_dict(jobs_dataframe,  orient='index')
        # df.to_csv = ('jobs_data.csv')
        # df.to_csv= ('/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/Indeed/Indeed')
        # print(df)
        # print(self.job_data)
        # df = pd.DataFrame.from_dict(self.job_data, orient='index')
        
        # df.to_csv('jobs_dataframe.csv', index=True)
        # df.to_csv = (r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/Indeed/Indeed')
        # print(df)
        # return df
    def connect_to_db(self):
        end_point = 'database-1.c3qa23m8pxdu.eu-west-2.rds.amazonaws.com'
        dbname = 'my_database'
        port = 5432
        user_name = 'postgres'
        password = 'Database123!'
        conn = None
        cur = None
        
        try: 
            conn = ps.connect(host = end_point, database = dbname, user = user_name,password = password, port= port )
                
            cur = conn.cursor()
            # df1 = pd.read_csv('job_indeed.csv')
            # file = "job_indeed.csv"
            # clean_table_name = file.lower().replace(" ", "").replace("?", "").replace(" ", "_")
            SQL_table= """create table dataframe_indeed
                (Job_URL                varchar,
                Unique_ID               varchar, 
                Job_Title               varchar,
                Name_of_the_company     varchar,
                Company_Location        varchar,
                Salary_package          varchar);"""
            
            replacements = """{ 'object' : 'varchar',
                            'float64' : 'float',
                            'int64' : 'int',
                            'datetime64' : 'datestamp', 
                            'timedelta64(ns)': 'varchar'
                            }
                """
            # print(SQL_table)
            
            cur.execute("drop table if exists dataframe_indeed.csv") 
            
            cur.execute("create table dataframe_indeed (Job_URL varchar, ID varchar, Job_Title varchar, Name_of_the_company varchar, Company_Location varchar, Salary_package varchar)")
            print('table created')
            # csv_files =[]
            # for file in os.listdir(os.getcwd()):
            #     if file.endswith('.csv'):
            #         csv_files.append(file)
                    # print(csv_files)
            
            # my_file = open('dataframe_indeed.csv', encoding='utf-8')
            # print('file opened in memory')
            
            # SQL_STATEMENT = """
            # COPY df FROM STDIN WITH 
            # CSV
            # HEADER
            # DELIMITER AS ','
            # """
            
            # cur.copy_expert(sql=SQL_STATEMENT, file=my_file)
            # print('file copied to db')
            # create_data = (r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/df.csv')
            # cur.execute(create_data)
            # conn.commit()
                 
        except ps.OperationalError as error:
            print(error)
        
            
        else:
            print('Connected!')
            return conn
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()
        
        # data_paths = [os.path.join(jobs_dataframe, f) for f in os.listdir(jobs_dataframe)]
        # data_paths = [i for i in data_paths if os.path.isfile(i)]
        # df.to_csv(r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/Indeed/Indeed', index=index, header=True)
        
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
            list_of_all_jobs_details.append(job_details_dictionary)
            global jobs_dataframe
            jobs_dataframe = dict()
            jobs_dataframe = {"Job_URL": job_details_dictionary["Job_Link"],
                        'ID':job_details_dictionary['Unique_ID'], 
                        'Job_Title': job_details_dictionary['Title'],
                        'Name_of_the_company': job_details_dictionary['Company_Name'],
                        'Location': job_details_dictionary['Company_Location']}
                    # 'Salary Package': job_details_dictionary['Salary']}
            # print(jobs_dataframe)
            # print(jobs_dataframe)
            # df = pd.DataFrame.from_dict(jobs_dataframe,  orient='index')
            # df.to_csv = ('df.csv')
            # df.to_csv= ('/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/Indeed/Indeed')
            # print(df)
            # # print(list_of_all_jobs_details)
        return list_of_all_jobs_details
        
        
    
       
    # list_of_jobs = get_job_details(s)
    # print(list_of_jobs)
    
    # def sql_table(self):
    #     create table 
    #     (Job_URL                sqlalchemy.VARCHAR
    #      ID                     sqlalchemy.VARCHAR, 
    #     Job_Title               sqlalchemy.VARCHAR,
    #     Name_of_the_company     sqlalchemy.VARCHAR,
    #     Company_Location        sqlalchemy.VARCHAR,
    #     Salary_package          sqlalchemy.VARCHAR);
        
    #     replacements = { 'object' : 'varchar',
    #                     'float64' : 'float',
    #                     'int64' : 'int',
    #                     'datetime64' : 'datestamp', 
    #                     'timedelta64(ns)': 'varchar'
    #                     }
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
        self.get_dataframe()
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

        