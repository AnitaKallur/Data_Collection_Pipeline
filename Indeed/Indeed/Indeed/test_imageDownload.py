import unittest
import selenium 
from indeed_scraper_main import Scraper


class TestImageLoad(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.scraper = Scraper()
  
    def test_downloadImage(self):
        try:
            expected_value = 'image'
            actual_value = len(self.scraper.download_image())
            self.assertEqual(expected_value, actual_value)
        except AssertionError as msg:
            print(msg)
        
    @classmethod
    def tearDownClass(self) -> None:
        del self.scraper
if __name__ == "__main__":
    unittest.main()