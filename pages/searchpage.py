from selenium.webdriver.common.by import By


# Interface for Google Search Page
# Stores page specific information in one place for ease of use and modification
class SearchPage:

    page_url = "https://www.google.com/search"
    title_suffix = "Google Search"

    search_results = {
        "by": By.XPATH,
        "value": "//div[@class='g']",
        "name": "Search Results"
    }
    search_results_links = {
        "by": By.XPATH,
        "value": "//div[@class='g']//h3/parent::a",
        "name": "Search Results links"
    }
