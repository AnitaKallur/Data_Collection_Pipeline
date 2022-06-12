from selenium import webdriver
import requests
import json
from numpy import product
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from numpy.random import randn
import numpy as np
from time import sleep
import io
from io import StringIO
from PIL import Image 
import pandas as pd
# driver = webdriver.Chrome()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url=driver.get("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=Greater%20London&vjk=f11971796d62ded9")
job_containers = driver.find_elements(by=By.XPATH, value="//ul[@class='jobsearch-ResultsList']//div[@class='slider_container css-11g4k3a eu4oa1w0']")
# image_url = "https://uk.indeed.com/jobs?q=Data%20Engineer%20or%20Data%20Scientist%20&l=London%2C%20Greater%20London&vjk=63c92ffb71fad229&advn=9660210449134183"
def get_job_details(details_container: list):
    list_of_all_jobs_details = []
    for job_listing in details_container:
        job_details_dictionary = dict()
        job_details_dictionary["Job Link"] = job_listing.find_element(by=By.XPATH, value=".//a").get_attribute('href')
        job_details_dictionary["Unique ID"] = job_listing.find_element(by=By.XPATH, value=".//a").get_attribute('id')
        sleep(2)
        job_details_dictionary["Title"] = job_listing.find_element(by=By.XPATH, value=".//h2").text
        job_details_dictionary["Company Name"] = job_listing.find_element(by=By.XPATH, value=".//div/span[@class='companyName']").text
        job_details_dictionary["Company Location"] = job_listing.find_element(by=By.XPATH, value=".//div[@class='companyLocation']").text
        try:
            job_details_dictionary["Salary"] = job_listing.find_element(by=By.XPATH, value= ".//div[@class='metadata salary-snippet-container']").get_attribute('textContent')
        except:
            pass
        # try:
        #     job_details_dictionary["Image"] = job_listing.find_element(by=By.XPATH, value= ".//div[@class='jobsearch-JobComponent-embeddedHeader']").get_property('src')
        # except Exception as NoSuchElement:
        #     print(NoSuchElement)
               
    
        list_of_all_jobs_details.append(job_details_dictionary)
    return list_of_all_jobs_details
list_of_jobs = get_job_details(job_containers)
# print(list_of_jobs)

# def download_image(download_path,url, file_name):
#     image_url = "https://uk.indeed.com/jobs?q=Data%20Engineer%20or%20Data%20Scientist%20&l=London%2C%20Greater%20London&vjk=63c92ffb71fad229&advn=9660210449134183"
#     image_content = requests.get(url).content
#     image_file = io.BytesIO(image_content)
#     image = image.open(image_content)
#     file_path = download_path + file_name
#     with open(file_path, "wb") as f:
#         image.save(f, "JPEG")
#     print("IMAGE")
# download_image(" ",image_url, "image.jpg" )
    # print(dir(driver))
# with open("jobs.json", "w") as outfile:
#     json.dump(list_of_jobs, outfile, indent=4)
            
df = pd.DataFrame(data= list_of_jobs, columns=(['Job Link', 'Unique ID', 
                                                'Title', 'Company Name', 
                                                'Company Location', 'Salary']))
# print(df)




iris = sns.load_dataset('iris')
iris.head()




driver.quit()



