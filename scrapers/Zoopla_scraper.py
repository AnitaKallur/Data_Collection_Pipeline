

from numpy import product
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
from time import sleep
import uuid
uuid4 = uuid.uuid4()


class scraper:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.url = self.driver.get("https://www.zoopla.co.uk/for-sale/houses/station/rail/sidcup/?beds_min=2&page_size=25&price_max=10000000&property_sub_type=detached&property_sub_type=bungalow&property_sub_type=semi_detached&view_type=list&q=Sidcup%20Station%2C%20Kent&radius=1&results_sort=newest_listings&search_source=refine")
        self.driver.implicitly_wait(10)
        #self.driver.maximize_window()
        
        """ self.driver.implicitly_wait(10) 
        self.url_bs4 = 'https://www.zoopla.co.uk/for-sale/houses/station/rail/sidcup/?beds_min=2&page_size=25&price_max=10000000&property_sub_type=detached&property_sub_type=bungalow&property_sub_type=semi_detached&view_type=list&q=Sidcup%20Station%2C%20Kent&radius=1&results_sort=newest_listings&search_source=refine'
        self.response = requests.get(self.url_bs4, cookies = {'Accept all cookies': 'yes'})
        self.soup = BeautifulSoup(self.response.text, "html.parser")  """
        
    def nevigate_page(self) -> None:
        sleep(3)
        print('start')
        print('GoodLuck')
        cookie_btn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div/span[contains(text(),'Accept all cookies')]")))
        print(cookie_btn)
        print('go')
        sleep(2)
    
        print('stop')
        print(type(cookie_btn))
        cookie_btn.click()
        
        #self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
     
        """ self.accept_cookies = self.driver.find_element('xpath', "//div/span[contains(text(),'Accept all cookies')]")
        sleep(3)
        self.accept_cookies.click() """
        """ for el in self.accept_cookies:
            if el.text == 'Accept all cookies':
                new_button = el
        new_button.click() """
            #self.driver.quit() 
        
        
    """ self.third_element = self.driver.find_element(by=By.XPATH, value= "//div[@class='heading4 color-text-primary singleLineTitle tapItem-gutter']")
        self.third_element.click()
        sleep(3)

        
    
    def page_links(self) -> None:
        try:
            self.elements = self.driver.find_elements(by=By.XPATH, value= "//a[@class='jcs-JobTitle']")
            sleep(5)
            self.uid_item = self.driver.find_elements(by=By.XPATH, value= "//a[@class='jcs-JobTitle']")
            sleep(5)
            while True:
                
                for element in self.elements:
                    self.elements_links= element.get_property('href')
                    sleep(1)
                    print(self.elements_links)
                    #self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight/3.4);')
                    
                    #print(self.uid_list, self.elements_links)
                for l in self.uid_item:
                    self.uid_list = l.get_attribute('id')
                    sleep(1)
                    #self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight/3.4);')
                    print(self.uid_list)
                break  
                #elements_links = []
        except Exception as ex:
            pass
                
    def UUID_products(self):
        self.products_elements = self.driver.find_elements(by=By.XPATH, value="//table[@class='jobCardShelfContainer big6_visualChanges']")  
        for element in self.products_elements:
            self.product_features = element.get_attribute('aria-label')
            print(self.product_features)
        #self.driver.quit() """
    def main(self) -> None:
        self.nevigate_page()
        #self.page_scroll()
        #self.page_links()
        #self.UUID_products()

        #self.driver.quit()
if __name__ == "__main__":
    DPS = scraper()
    DPS.main()

         