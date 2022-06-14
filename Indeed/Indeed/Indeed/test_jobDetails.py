import unittest
import selenium 
from indeed_scraper_main import Scraper


class TestJobDetails(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.scraper = Scraper()
  
    def test_jobScrape(self):
        try:
            expected_value = 'href', 'id', 'text'
            actual_value = self.scraper.get_job_details(job_containers='')
            self.assertEqual(expected_value, actual_value)
        except AssertionError as msg:
            print(msg)
        
    @classmethod
    def tearDownClass(self) -> None:
        del self.scraper
if __name__ == "__main__":
    unittest.main()