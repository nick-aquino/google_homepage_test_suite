from selenium.webdriver.common.by import By


# Interface for Google Homepage
# Stores page specific information in one place for ease of use and modification
class HomePage:

    page_url = "https://www.google.com/"
    title = "Google"

    # Elements by, value, and name
    logo = {
        "by": By.ID,
        "value": "hplogo",
        "name": "Google Logo"
    }
    search_btn_static = {
        "by": By.XPATH,
        "value": "//div[@class='FPdoLc VlcLAe']//input[@name='btnK']",
        "name": "Google Search Button Static"
    }
    search_btn_dropdown = {
        "by": By.XPATH,
        "value": "//div[@class='UUbT9']//input[@name='btnK']",
        "name": "Google Search Button Dropdown"
    }
    search_text = {
        "by": By.NAME,
        "value": "q",
        "name": "Search Text Box"
    }
