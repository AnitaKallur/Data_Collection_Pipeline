import pandas as pd
import os
import numpy as np
import psycopg2
from operator import index
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


records = []
""" This class scrapes the website and files the details in a json file"""

class Scraper:
    """Using webdriver to automate the webpage"""
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.url = self.driver.get("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=Greater%20London&vjk=f11971796d62ded9")
        self.url_bs = ("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=Greater%20London&vjk=f11971796d62ded9")
        
        
        
        self.job_containers = self.driver.find_elements(by=By.XPATH, value="//ul[@class='jobsearch-ResultsList']//div[@class='slider_container css-11g4k3a eu4oa1w0']")
        self.driver.maximize_window()
        
        
        
        
    def get_record(self): 
        # url = response.get("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=Greater%20London&vjk=f11971796d62ded9")
        
        while True:   
            pagination = self.driver.find_element(by=By.XPATH, value="//a[@aria-label='Next']").click()
            self.response = requests.get(self.url_bs)
            self.soup = bs(self.response.text, "html.parser")
            # self.response = requests.get(self.url_bs)
            cards = self.soup.find_all('div', 'jobsearch-SerpJobCard')
            pagination += 1
            for card in cards:
                self.record = self.get_record(card)
                records.append(self.record)
            print(len(records))
            try:
                self.pagination = 'https://www.indeed.com'+ self.soup.find('a', {'aria-label': 'Next'}).get('href')
                # self.pagination.click()
            except AttributeError:
                break
        
        
        
            
            
    def nevigate_page(self) -> None:
        """ This will accept all cookies """
        # self.close_popup = self.driver.find_element(by=By.XPATH, value="//button[@onclick='closeGoogleOnlyModal()']")
        self.accept_cookies = self.driver.find_element(by=By.XPATH, value= "//button[@id='onetrust-accept-btn-handler']")
        self.accept_cookies.click()
        self.third_element = self.driver.find_element(by=By.XPATH, value= "//div[@class='heading4 color-text-primary singleLineTitle tapItem-gutter']")
        self.third_element.click()
        sleep(3)
        self.fourth_element = self.driver.find_element(by=By.XPATH, value="//td[@class='resultContent']")
    
    
    def scrape(self):
        """Assigning a new method to call another method"""
        # self.nevigate_page()
        # self.__get_job_details(self.job_containers)
        job_indeed= self.get_job_details(self.job_containers)
        save_path = '/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline'
        if not os.path.exists(f'{save_path}/Indeed_Data_New'):
                os.makedirs(f'{save_path}/Indeed_Data_New')

        with open(f'{save_path}/Indeed_Data_New/Data_New.json', 'w+') as fp:
            json.dump(job_indeed, fp,  indent=4)
        global df
        df = pd.DataFrame.from_dict(job_indeed) 
        df.to_csv(r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/data_jobs_New.csv', 
        index = False, header=True)
        print(df)
        if os.path.exists(f'{save_path}/Indeed_Data_New/data_jobs_New.csv') and os.path.exists(f'{save_path}/Indeed_Dataframe/Data_jobs.json'):
            self.saving_data = True
            return self.saving_data, save_path
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
            # print(list_of_all_jobs_details)
        return list_of_all_jobs_details
    def main(self) -> None:
        self.nevigate_page()
        
        self.scrape()
        # print(self.scrape())
        # self.download_image()
        # print(self.download_image())
        # self.get_dataframe()
        # print(self.get_dataframe)
        # self.connect_to_db()
        self.get_record()
        # self.get_job_details(job_containers=)
        self.driver.quit()
        
if __name__ == "__main__":
    DPS = Scraper()
    DPS.main()


# df = pd.read_csv('df.csv')
# df.head()
# # df.to_csv(r'/Users/prabhuswamikallur/Desktop/Data_Collection_Pipeline/job_indeed.csv')
# df=df.loc[:, ~df.columns.str.contains('^Unnamed')]
# # df.drop('Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', axis=1, inplace=True)
# print(df)

# os.getcwd()
# print(os.getcwd())
