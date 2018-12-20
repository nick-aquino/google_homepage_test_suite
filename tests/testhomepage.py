from selenium import webdriver
from tools.testhelper import TestHelper
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.homepage import HomePage
from pages.searchpage import SearchPage


class TestHomePageCases:

    class TestHomePage(TestHelper):

        # Defaulting to Firefox
        driverclass = webdriver.Firefox

        # Sets up clean environment before each test
        def setUp(self):

            self.driver = self.driverclass()
            self.driver.get(HomePage.page_url)

        # 1. The Google logo image is present.
        def test_1_google_logo(self):

            self.check_element_present(**HomePage.logo)

        # 2. The Search text field is present.
        def test_2_text_field(self):

            self.check_element_present(**HomePage.search_text)

        # 3. The Google Search button is present.
        def test_3_search_btn(self):

            self.check_element_present(**HomePage.search_btn_static)

        # 4. Search text may be entered into the Search text field (e.g. 'True Fit')
        def test_4_text_field_input(self):

            search_text = self.find_element(**HomePage.search_text)
            self.send_keys_to_element(search_text, "True Fit")

        # 5. Clicking the 'Google Search' button with search text yields search results.
        def test_5_search_text(self):

            search_text = self.find_element(**HomePage.search_text)
            self.send_keys_to_element(search_text, "True Fit")

            # Using locator for 'Google Search' button that appears in predictive text dropdown
            search_btn = self.find_element(**HomePage.search_btn_dropdown)

            # Wait for button to appear then click
            WebDriverWait(self.driver, 5).until(ec.visibility_of(search_btn))
            search_btn.click()

            # wait for search page url
            WebDriverWait(self.driver, 5).until(ec.url_contains(SearchPage.page_url))

            # assert search page title
            self.assertTrue(self.driver.title == 'True Fit - '+SearchPage.title_suffix)

            # helper method for verifying element list is not empty
            self.find_element_list(**SearchPage.search_results)

        # 6. Clicking the 'Google Search' button with no search text will not perform a search.
        def test_6_search_no_text(self):

            search_btn = self.find_element(**HomePage.search_btn_static)
            search_text = self.find_element(**HomePage.search_text)

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


class TestHomePageChrome(TestHomePageCases.TestHomePage):
    # override driver with Chrome Driver
    driverclass = webdriver.Chrome


class TestHomePageFirefox(TestHomePageCases.TestHomePage):
    # override driver with Firefox Driver
    driverclass = webdriver.Firefox
