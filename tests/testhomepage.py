from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.homepage import HomePage
from pages.searchpage import SearchPage
import unittest
from tools.driverhelper import DriverHelper


class TestHomePage(unittest.TestCase, DriverHelper):

    # Sets up environment before each test
    def setUp(self):

        # gets driver class from DriverHelper then instantiates
        self.driver = DriverHelper.get_driver(self)()
        self.driver.get(HomePage.page_url)

    # 1. The Google logo image is present.
    def test_1_google_logo(self):

        try:
            google_logo = self.driver.find_element(*HomePage.logo)
            self.assertTrue(google_logo.is_displayed())
        except NoSuchElementException:
            self.fail("Google logo not found")

    # 2. The Search text field is present.
    def test_2_text_field(self):

        try:
            search_text = self.driver.find_element(*HomePage.search_text)
            self.assertTrue(search_text.is_displayed())
        except NoSuchElementException:
            self.fail("Search text field not found")

    # 3. The Google Search button is present.
    def test_3_search_btn(self):

        try:
            search_btn = self.driver.find_element(*HomePage.search_btn_static)
            self.assertTrue(search_btn.is_displayed())
        except NoSuchElementException:
            self.fail("Google Search button not found")

    # 4. Search text may be entered into the Search text field (e.g. ‘True Fit’)
    def test_4_text_field_input(self):

        search_text = self.driver.find_element(*HomePage.search_text)
        search_text.send_keys("True Fit")
        self.assertTrue(search_text.get_attribute("value") == "True Fit")

    # 5. Clicking the ‘Google Search’ button with search text yields search results.
    def test_5_search_text(self):

        search_text = self.driver.find_element(*HomePage.search_text)
        search_text.send_keys("True Fit")

        search_btn = self.driver.find_element(*HomePage.search_btn_static)
        search_btn.click()

        # wait for search page url
        WebDriverWait(self.driver, 5).until(ec.url_contains(SearchPage.page_url))

        # assert search page title
        self.assertTrue(self.driver.title == 'True Fit - '+SearchPage.title_suffix)

        # assert search results elements exists
        # check size of array since find_elements does not throw exception when no results are found
        search_results = self.driver.find_elements(*SearchPage.search_results)
        self.assertTrue(len(search_results) > 0)

    # 6. Clicking the ‘Google Search’ button with no search text will not perform a search.
    def test_6_search_no_text(self):

        search_btn = self.driver.find_element(*HomePage.search_btn_static)
        search_text = self.driver.find_element(*HomePage.search_text)

        # verify search text is empty
        self.assertTrue(search_text.get_attribute("value") == "")

        # submit without any search text
        search_btn.click()

        try:
            WebDriverWait(self.driver, 5).until(ec.url_contains(SearchPage.page_url))
        except TimeoutException:
            # URL did not change, Check that title matches HomePage title
            self.assertTrue(self.driver.title == HomePage.title)
            return
        self.fail("Google performed a search")

    def tearDown(self):
            self.driver.quit()
