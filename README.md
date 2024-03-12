
# Automated Testing

This project explains automated tests for searching images on the Unsplash website using Selenium.

### Initial Stage

what we need for the assignment

* Python 3.x
* Selenium library
* Chrome Webdriver installation

### Installation

1. Cloning the repository to your local machine:
git clone https://github.com/your_username/unsplash-search-test.git

2. Installing the required dependencies using pip:
 pip install selenium

Making changes in environmental variables (system variables) editing path

## Test Details
### Test Case: Testing Search panel for Images given the term "book"

* **Description** : Searches for images related to the term "book" on the website we chose.

* **Automation tool** :  For browser automation, we use Selenium WebDriver

* **Setup** : Initializes a Chrome WebDriver and navigates to the  website.

* **Search** : Enter the search phrase "book" into the search input form and hit Enter.

* **Verification** : The test waits for the search results to load before determining whether the search term "book" is present in the page source.

* **Teardown** : After the test is completed, the WebDriver instance is closed.



class UnsplashWebsiteSearchTest(unittest.TestCase):
    def setUp(self):
        self.browser_driver = webdriver.Chrome()
        self.browser_driver.implicitly_wait(10)
        self.browser_driver.get("https://unsplash.com/")

    def test_search_book(self):
        # Test implementation...
        pass

    def tearDown(self):
        self.browser_driver.quit()

### 1. Test class definition

The class **UnsplashWebsiteSearchTest(unittest.TestCase)** This generates a test class named UnsplashWebsiteSearchTest, which derives from **unittest.TestCase**, the base class for all test cases in the unittest framework.


### 2. Test Setup Mode

**setUp(self)**: This method is invoked before any test methods are executed. It launches the web browser (Chrome WebDriver), sets an implicit wait time of ten seconds, and navigates to the Unsplash website.

### 3. Test method

**test_search_book(self)**: This is a test method that details how to test the functionality of searching for images labeled with "book" on the Unsplash website. The code snippet provided does not include the actual implementation of the test stages, which would typically include interactions with site elements, assertions, and verifications.


### 4. Test teardown method

**tearDown(self): This method is invoked once each test method is completed. It terminates the web browser session to save up resources.

if __name__ == "__main__":
    unittest.main()

### main block 

if __name__ == "__main__": This block ensures that the tests are run only when the script is executed directly, rather than when it is imported as a module. To run the test suite, it calls unittest.main().







