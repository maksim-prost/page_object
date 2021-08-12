from typing import cast
from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CLASS_NAME, 'btn-group')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    FORM_LOGIN = (By.ID, "login_form")
    FORM_REGISTER = (By.ID, "register_form")
    INPUT_REGISTER = ( By.CSS_SELECTOR, '.register_form  input')
    INPUT_EMAIL = (By.NAME, 'registration-email')
    INPUT_PASSWORD1 = (By.ID, 'id_registration-password1')
    INPUT_PASSWORD2 = (By.ID, 'id_registration-password2')
    BUTTON_REGISTER = ( By.NAME, 'registration_submit')

class AddBasketPageLocators():
    BUTTON_BASKET = ( By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_NAME_PRODUCT = ( By.CSS_SELECTOR, ".alertinner strong")
    PRICE_BASKET = ( By.CSS_SELECTOR,".alert-info strong")
    NAME_PRODUCT = ( By.CSS_SELECTOR, ".product_main  h1")
    PRICE_PRODUCT = ( By.CSS_SELECTOR, ".product_main  p")
    MESSAGE_SUCCES = ( By.CLASS_NAME, 'alert-success')

class BasketPageLocators():
    BASKET_ITEMS = ( By.CLASS_NAME, 'basket-items')
    MESSAGE_EMPTY_BASKET = ( By.CSS_SELECTOR, '#content_inner p')