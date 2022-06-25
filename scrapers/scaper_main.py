
from lib2to3.pgen2 import driver
from typing_extensions import Self
from selenium import webdriver
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

class scraper:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.url = self.driver.get("https://www.amazon.co.uk")
        self.driver.maximize_window()
        self.driver.implicitly_wait(100)
        
    def nevigate_page(self) -> None:
        
        #self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.first_element = self.driver.find_element(by=By.LINK_TEXT, value= 'Best Sellers')
        self.first_element.click()
        sleep(1)

        self.second_element = self.driver.find_element(by=By.NAME, value= 'accept')
        self.second_element.click()
        sleep(1)

        self.third_element = self.driver.find_element(by=By.XPATH, value= '//body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[8]/a[1]')
        self.third_element.click()
        sleep(3)

        """ self.fourth_element = self.driver.find_element(by=By.XPATH, value= '//a[contains(text(),2)]')
        self.fourth_element.click()
        time.sleep(3) """
    def page_scroll(self) -> None:
        
        self.last_height = self.driver.execute_script('return document.body.scrollHeight')
        sleep(3)
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        sleep(3)
        #new_height = driver.execute_script('return document.body.scrollHeight')
        #sleep(3)
        self.scroll_pause_time = 3
        i = 0
        self.number_of_scrolls = 3
        while i < self.number_of_scrolls:
            print(f"scrolled {i} time(s)")
            sleep(3)
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight/3.4);')
            sleep(3)
            sleep(self.number_of_scrolls)
            self.new_height = self.driver.execute_script(
                        "return document.body.scrollHeight")
            if self.new_height == self.last_height:
                break
            i += 1
            self.last_height = self.new_height
            
    def page_links(self) -> None:
        try:
            self.elements = self.driver.find_elements(by=By.XPATH, value="//a[@class='a-link-normal' and (@tabindex='-1' and @role='link')]")
            sleep(5)
            self.uid_item = self.driver.find_elements(by=By.XPATH, value= "//div[@class='a-cardui _cDEzb_grid-cell_1uMOS p13n-grid-content']")
            sleep(5)
            while True:
                for l in self.uid_item:
                    self.uid_list = l.get_attribute('id')
                    #print(self.uid_list)
                for element in self.elements:
                    self.elements_links= element.get_property('href')
                    #print(self.uid_list)
                    self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight/3.4);')
                    #sleep(3)
                    print(self.uid_list, self.elements_links)
                #elements_links = []
        except Exception as ex:
            pass
                
            
        
        self.driver.quit()
    def main(self) -> None:
        self.nevigate_page()
        self.page_scroll()
        self.page_links()


if __name__ == "__main__":
    DPS = scraper()
    DPS.main()

        