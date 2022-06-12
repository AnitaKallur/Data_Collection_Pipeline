from numpy import product
from selenium import webdriver
from bs4 import BeautifulSoup
import requests, openpyxl

""" excel = openpyxl.Workbook()
sheet = excel.active
sheet.title ='Top rated TVshows'
print(excel.sheetnames)
sheet.append(['Show Rank', 'Show Name', 'Year of Release', 'IMBD Rating']) """
import re
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
from time import sleep

import uuid
uuid4 = uuid.uuid4()
# print(list_of_jobs)
    # list_of_jobs = get_job_details(details_container=self.job_containers)
    # print(list_of_jobs)
    # with open("jobs.json", "w") as outfile:
    #     json.dump(list_of_jobs, outfile, indent=4)
    
        # # self.indeed_dict= dict()
        # try:
        #     #Get links from the page
        #     self.elements = self.driver.find_elements(by=By.XPATH, value= "//a[@class='jcs-JobTitle']")
        #     sleep(2)
        # except:
        #     self.elements = 'None'
        # #     pass
        # try:
        #     #Get unique ID of the product
        #     self.uid_item = self.driver.find_elements(by=By.XPATH, value= "//a[@class='jcs-JobTitle']")
        #     sleep(2)   
        # except:
        #     self.uid_item = 'None'
        #     #Get job title 
        # try:
        #     self.title = self.driver.find_elements(by=By.XPATH, value='//span[@title]')
        #     sleep(2)  
        # except:
        #     self.title = 'None'
        # #     #Get company name
        # try:
        #     self.companyName = self.driver.find_elements(by=By.XPATH, value= "//span[@class='companyName']")
        #     sleep(2)   
        # except:
        #     self.companyName = 'None'
        # try:
        #     self.companyLocation = self.driver.find_elements(by=By.XPATH, value= "//div[@class='companyLocation']")
        #     sleep(2)
        # except:
        #     self.company_location = 'None'
        # try:
        #     self.salary = self.driver.find_elements(by=By.XPATH, value= "//div[@class='metadata salary-snippet-container']")
        #     sleep(2)
        # except:
        #     self.salary = 'None'
            
        # try:    
        #     self.jobDescription = self.driver.find_elements(by=By.XPATH, value="//table[@class='jobCardShelfContainer big6_visualChanges']")
        #     sleep(3)
        #     # for i in self.jobDescription:
        #     #     self.job_description = i.text
        #     #     print(self.job_description)
            
        #     # self.job_Description = self.driver.find_element(by=By.XPATH, value="//div[@id='jobDescriptionText']").get_attribute('textContent')
        #     # print(self.job_Description.text)
        #     sleep(3)
        # except:
        #     self.jobDescription = 'None'
            
            
        # while True:
                
        #     for element in self.elements:
        #         self.elements_links= element.get_property('href')
        #         sleep(1)
        #         self.indeed_dict['job_links'].append(self.elements_links)
        #         # self.dataframe = pd.concat({'job_links': self.elements_links }, ignore_index=True)
        #         # print(self.elements_links)
        #     for l in self.uid_item:       
        #         self.uid_list = l.get_attribute('id')
        #         sleep(1)
        #         self.indeed_dict['unique_id'].append(self.uid_list)
        #         # print(self.uid_list)
        #         # self.dataframe = pd.concat({'unique_id': self.uid_list}, ignore_index=True)
        #     for t in self.title:
        #         self.elements_title = t.get_property('textContent')
        #         sleep(1)
        #         self.indeed_dict['title'].append(self.elements_title)
        #         # print(self.elements_title)
        #         # self.dataframe = pd.concat({'title': self.elements_title }, ignore_index=True)  
        #     for name in self.companyName:
        #         self.company_name = name.get_property("textContent")
        #         sleep(1)
        #         self.indeed_dict['comp_name'].append(self.company_name)
        #         # print(self.company_name)
        #         # self.dataframe = pd.concat({'comp_name': self.company_name}, ignore_index=True)    
        #     for location in self.companyLocation:
        #         self.company_location = location.get_property("textContent")
        #         sleep(1)
        #         # self.dataframe = pd.concat({'comp_location': self.company_location }, ignore_index=True)
        #         self.indeed_dict['comp_location'].append(self.company_location)
        #         # print(self.company_location)
        #     for sal in self.salary:
        #         self.salary_Package = sal.get_property("textContent")
        #         sleep(1)
        #         self.indeed_dict['sal_package'].append(self.salary_Package)
        #         # print(self.salary_Package)
        #     # self.dataframe = pd.concat({'sal_package': self.salary_Package }, ignore_index=True)
        #     for job in self.jobDescription:
        #         self.job_description = job.get_property('textContent')
        #         sleep(2)
        #         self.indeed_dict['job_details'].append(self.job_description)
                
        #         print(f"Company URL: " ,{self.elements_links}, 
        #               f"Company Name: ",{self.company_name}, 
        #               f"Company Unique ID: ",{self.uid_list}, 
        #               f"Company Location: ",{self.company_location}, 
        #               f"Job Title: ",{self.elements_title} ,
        #               f"Salary Package: ",{self.salary_Package} ,
        #               f"Job Details: ",{self.job_description}).__format__
        #     print()
        #     break
            
    # def get_logo(self):    
    #     indeed_image = self.driver.find_elements(by=By.XPATH, value="//div/img[@class='jobsearch-JobInfoHeader-logo jobsearch-JobInfoHeader-logo-overlay-lower']")
    #     for image in indeed_image:
    #         self.get_image = image.get_attribute("src")
    #         self.indeed_dict['comp_logo'].append(self.get_image)
            # print(len(self.get_image))
        # self.dataframe = pd.concat({'comp_logo': self.get_image }, ignore_index=True)
       
    # def indeed_full_data(self):
    #     save_data = ['Job Link', 'Job ID', 'Job Title', 'Company Name', 'Company Location', 'Salary Package', 'Job Description', 'Company logo']
    #     # indeed_data = {'unique_id': {'job_links', 'job_title', 'comp_name', 'comp_location', 'sal_package', 'job_details', 'collect_logo'}}
        
    #     # self.dataframe = pd.concat({'job_links': self.elements_links, 'unique_id': self.uid_list, 'title': self.elements_title, 'comp_name': self.company_name, 'comp_location': self.company_location, 'sal_package': self.salary_Package, 'job_details': self.job_description}, ignore_index=True)
    #     # df1 = pd.DataFrame(self.indeed_dict, columns= ['Job Link', 'Job ID', 'Job Title', 'Company Name', 'Company Location', 'Salary Package', 'Job Description', 'Company logo'])
    #     # with open("Indeed_Data", "w") as fp:
    #     #     fp.write(df1)
        
        
    #     with open("Indeed_Scraper_Data", "w") as fp:
    #         json.dumps(self.indeed_dict, fp, indent=4)
    #         # fp.write(df)
    #     # self.dataframe.to_csv("IndeedScraper.csv", index=False)
    #     # df1 = pd.read_csv('indeed_dict.csv', encoding="utf-8")
      