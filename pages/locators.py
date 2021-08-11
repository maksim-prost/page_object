from typing import cast
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    FORM_LOGIN = (By.ID, "login_form")
    FORM_REGISTER = (By.ID, "register_form")

class AddBasketPageLocators():
    BUTTON_BASKET = ( By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_NAME_PRODUCT = ( By.CSS_SELECTOR, ".alertinner strong")
    PRICE_BASKET = ( By.CSS_SELECTOR,".alert-info strong")
    NAME_PRODUCT = ( By.CSS_SELECTOR, ".product_main  h1")
    PRICE_PRODUCT = ( By.CSS_SELECTOR, ".product_main  p")
    MESSAGE_SUCCES = ( By.CLASS_NAME, 'alert-success')