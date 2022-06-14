import unittest
from selenium import webdriver
import page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from indeed_scraper_main import nevigate_page

class IndeedJobScraper(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://uk.indeed.com/jobs?q=data%20engineer%20or%20data%20scientist&l=Greater%20London&vjk=f11971796d62ded9")
        
    
    def test_nevigate_page(self):
        self.assertTrue()
        
        
        
    def tearDown(self) -> None:
        self.driver.close()
        
        
if __name__ == "__main__":
    unittest.main()