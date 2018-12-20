from selenium.common.exceptions import NoSuchElementException
import unittest


class TestHelper(unittest.TestCase):

    # uses internal find element and checks that element is displayed
    def check_element_present(self, by, value, name):
        element = self.find_element(by, value, name)
        self.assertTrue(element.is_displayed())

    # sends keys and asserts element value changed
    def send_keys_to_element(self, element, keys):
        element.send_keys(keys)
        self.assertTrue(element.get_attribute("value") == keys)

    # finds element and handles exception
    def find_element(self, by, value, name):
        try:
            element = self.driver.find_element(by, value)
            return element
        except NoSuchElementException:
            self.fail(name + " not found")

    # finds elements and checks that results are not empty
    def find_element_list(self, by, value, name):
        search_results = self.driver.find_elements(by, value)
        self.assertTrue(len(search_results) > 0, name + " list is empty")
        return search_results
