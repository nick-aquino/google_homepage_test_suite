from selenium.webdriver.common.by import By


# Interface for Google Search Page
# Stores page specific information in one place for ease of use and modification
class SearchPage:
    page_url = "https://www.google.com/search"
    title_suffix = "Google Search"

    search_results = (By.XPATH, "//div[@class='g']")
    search_results_links = (By.XPATH, "//div[@class='g']//h3/parent::a")
