import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

class UnsplashWebsiteSearchTest(unittest.TestCase):
    def setUp(self):
        self.browser_driver = webdriver.Chrome()
        self.browser_driver.implicitly_wait(10)
        self.browser_driver.get("https://unsplash.com/")

    def test_search_book(self):
        search_term = "book"
        try:
            # Locate the search input field
            search_input = WebDriverWait(self.browser_driver, 10).until(EC.presence_of_element_located((By.NAME, "searchKeyword")))
            # Enter the search term
            search_input.send_keys(search_term)
            # Press Enter key
            search_input.send_keys(Keys.RETURN)
            time.sleep(5)
            # Verify if the search term is present in the page source
            assert search_term in self.browser_driver.page_source
        except TimeoutException as e:
            # Print an error message if any timeout occurs
            print("Error:", e)

    def tearDown(self):
        self.browser_driver.quit()

if __name__ == "__main__":
    unittest.main()
