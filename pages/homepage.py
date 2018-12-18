from selenium.webdriver.common.by import By


# Interface for Google Homepage
# Stores page specific information in one place for ease of use and modification
class HomePage:

    page_url = "https://www.google.com/"
    title = "Google"

    logo = (By.ID, "hplogo")
    search_btn = (By.NAME, "btnK")
    search_text = (By.NAME, "q")
