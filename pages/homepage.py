from selenium.webdriver.common.by import By


# Interface for Google Homepage
# Stores page specific information in one place for ease of use and modification
class HomePage:

    page_url = "https://www.google.com/"
    title = "Google"

    logo = (By.ID, "hplogo")
    search_btn_static = (By.XPATH, "//div[@class='FPdoLc VlcLAe']//input[@name='btnK']")
    search_btn_dropdown = (By.XPATH, "//div[@class='UUbT9']//input[@name='btnK']")
    search_text = (By.NAME, "q")
