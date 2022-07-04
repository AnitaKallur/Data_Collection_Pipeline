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

def extract():
    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    s_url = driver.get("https://uk.indeed.com/jobs?q=Data%20Engineer%20or%20Data%20Scientist%20&l=London%2C%20Greater%20London&vjk=f11971796d62ded9")
    # url = (f'https://uk.indeed.com/jobs?q=Data%20Engineer%20or%20Data%20Scientist%20&l=London%2C%20Greater%20London&start={page}')
    # response = requests.get(url)
    # soup = bs(response.content, 'html.parser')
    # cards = soup.find_all('div', 'jobsearch-SerpJobcard')
    # pagination = driver.find_element(by=By.XPATH, value = "//a[@aria-label='2']")
    # pagination.click()
    
    # print()
    # print(response.json)
    # print(response.text)
    
    # print(cards)
# extract()
    # return soup
# def scrape(self, job_indeed):
#     """Assigning a new method to call another method"""
#     # self.nevigate_page()
#     # self.__get_job_details(self.job_containers)
#         # global job_indeed
#     job_indeed = self.get_job_details()
    
    
    
    
    
    
def get_job_details():
    
    """ Scraping all the details related to the job post"""
    list_of_all_jobs_details = []
    
    for job_listing in list_of_all_jobs_details:
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
        list_of_all_jobs_details.append(job_details_dictionary)
        print(list_of_all_jobs_details)
    return list_of_all_jobs_details
extract()
get_job_details()
print(get_job_details)
# extract(page='https://uk.indeed.com/jobs?q=Data%20Engineer%20or%20Data%20Scientist%20&l=London%2C%20Greater%20London&start=0')
# get_job_details()
# get_job_details()
# scrape(self=job_indeed)

# def transform(soup):
#     divs = soup.find_all('div', class_ = 'jobsearch-SerpJobCard')
#     # print(len(divs))
#     for item in divs:
#         title = item.find('a').text()
#         print(title)
#         company = item.find('span', class_ = 'company').text.strip()
#         summary = item.find('div', {'class': 'summary'}).text.strip()
#         try:
#             salary = item.find('span', class_ = 'salaryText').text.strip()
#         except:
#             salary = ' '
#         job = {
#             'title': title,
#             'company': company,
#             'salary': salary,
#             'summary': summary
#         }
#         joblist.append(job)
#     return
# joblist = []

# c = extract(0)

        
# c = extract(0)
# transform(c)
# print(joblist)
# print(c)