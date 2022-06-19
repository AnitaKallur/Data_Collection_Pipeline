import unittest
import selenium 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from indeed_scraper_main import Scraper

class test_allMethod(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.scraper = Scraper()
        
    def test_pageNavigate(self):
        try:
            expected_value = 'accept cookies'
            actual_value = self.scraper.nevigate_page()
            self.assertEqual(expected_value, actual_value)
        except AssertionError as msg:
            print(msg)
    def test_scrapeList(self):
        try:
            expected_value = 'job list'
            actual_value = self.scraper.scrape()
            self.assertEqual(expected_value, actual_value)
        except AssertionError as msg:
            print(msg)
    def test_jobScrape(self):
        try:
            actual_value = self.scraper.get_job_details(job_containers='')
            expected_value = 'id', 'href'
            self.assertEqual(expected_value, actual_value)
        except AssertionError as msg:
            print(msg)
            
    def test_downloadImage(self):
        try:
            expected_value = 'image'
            actual_value = self.scraper.download_image()
            self.assertEqual(expected_value, actual_value)
        except AssertionError as msg:
            print(msg)
    @classmethod
    def tearDownClass(self) -> None:
        del self.scraper
if __name__ == "__main__":
    unittest.main()