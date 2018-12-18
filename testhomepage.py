from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import unittest


class TestHomePage(unittest.TestCase):

    # Sets up environment before each test
    def setUp(self):

        # hard code Firefox for now
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.google.com")

    # 1. The Google logo image is present.
    def test_1_google_logo(self):

        try:
            self.driver.find_element_by_id("hplogo")
        except NoSuchElementException:
            self.fail("Google logo not found")

    # 2. The Search text field is present.
    def test_2_text_field(self):

        try:
            self.driver.find_element_by_name("q")
        except NoSuchElementException:
            self.fail("Search text field not found")

    # 3. The Google Search button is present.
    def test_3_search_btn(self):

        try:
            self.driver.find_element_by_name("btnK")
        except NoSuchElementException:
            self.fail("Google Search button not found")

    # 4. Search text may be entered into the Search text field (e.g. ‘True Fit’)
    def test_4_text_field_input(self):

        search_element = self.driver.find_element_by_name("q")
        search_element.send_keys("True Fit")
        self.assertTrue(search_element.get_attribute("value") == "True Fit")

    # 5. Clicking the ‘Google Search’ button with search text yields search results.
    def test_5_search_text(self):

        search_element = self.driver.find_element_by_name("q")
        search_element.send_keys("True Fit")
        search_element.submit()
        WebDriverWait(self.driver, 5).until(ec.title_contains("True Fit"))

        self.assertTrue(self.driver.title == 'True Fit - Google Search')

    # 6. Clicking the ‘Google Search’ button with no search text will not perform a search.
    def test_6_search_no_text(self):

        search_element = self.driver.find_element_by_name("q")
        # store current page title
        title_init = self.driver.title
        # submit without any search text
        search_element.submit()
        try:
            WebDriverWait(self.driver, 5).until(ec.title_contains("Google Search"))
        except TimeoutException:
            # Title did not change to "Google Search", check that it stayed the same
            self.assertTrue(self.driver.title == title_init)
            return
        self.fail("Google performed a search")

    def tearDown(self):
            self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHomePage)
    unittest.TextTestRunner(verbosity=2).run(suite)
