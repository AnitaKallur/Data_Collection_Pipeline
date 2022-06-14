import unittest
import selenium 
from indeed_scraper_main import Scraper


class TestNevigatePage(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.scraper = Scraper()
  
    def test_pageNavigate(self):
        try:
            expected_value = 'click'
            actual_value = self.scraper.nevigate_page()
            self.assertEqual(expected_value, actual_value)
        except AssertionError as msg:
            print(msg)
        
    @classmethod
    def tearDownClass(self) -> None:
        del self.scraper
if __name__ == "__main__":
    unittest.main()