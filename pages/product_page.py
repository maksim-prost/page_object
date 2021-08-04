from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import AddBasketPageLocators


class PageProduct(BasePage):

    def add_product_to_basket(self):
        name_product = self.browser.find_element(*AddBasketPageLocators.NAME_PRODUCT).text
        price_product = self.browser.find_element(*AddBasketPageLocators.PRICE_PRODUCT).text
        add_basket = self.browser.find_element(*AddBasketPageLocators.BUTTON_BASKET)
        add_basket.click()
        self.solve_quiz_and_get_code()
        self.check_add_product( name_product, price_product )


    def check_add_product( self, name_product, price_product ):
        message = self.browser.find_element(*AddBasketPageLocators.MESSAGE_NAME_PRODUCT).text
        assert message == name_product, "добавленной название не соответсвует исходному"
        
        price = self.browser.find_element(*AddBasketPageLocators.PRICE_BASKET).text
        print(price, "\n", price_product)
        assert price == price_product, f"добавленная цена  {price} не соответсвует исходной {price_product}"
        