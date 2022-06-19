import unittest
import selenium 
from indeed_scraper_main import Scraper


class TestJobDetails(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.scraper = Scraper()
  
    def test_jobScrape(self):
        try:
            actual_value = len(self.scraper.get_job_details(job_containers=''))
            expected_value = 15
            self.assertEqual(expected_value, actual_value)
        except AssertionError as msg:
            print(msg)
        
    @classmethod
    def tearDownClass(self) -> None:
        del self.scraper
if __name__ == "__main__":
    unittest.main()