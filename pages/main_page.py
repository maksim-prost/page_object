from .base_page import BasePage
# from selenium.webdriver.common.by import By
# from .locators import MainPageLocators

LINK_MAIN = link = "http://selenium1py.pythonanywhere.com"
class MainPage(BasePage):
    def __init__(self, browser, url=LINK_MAIN, timeout=1):
        super().__init__(browser, url, timeout=timeout) 

   