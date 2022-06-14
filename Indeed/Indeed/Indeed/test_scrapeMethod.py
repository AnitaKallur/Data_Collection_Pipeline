import unittest
import selenium 
from indeed_scraper_main import Scraper


class TestScrapeIndeed(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.scraper = Scraper()
  
    def test_scrapeList(self):
        try:
            expected_value = 'job list'
            actual_value = self.scraper.scrape()
            self.assertEqual(expected_value, actual_value)
        except AssertionError as msg:
            print(msg)
        
    @classmethod
    def tearDownClass(self) -> None:
        del self.scraper
if __name__ == "__main__":
    unittest.main()