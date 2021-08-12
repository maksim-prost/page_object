from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def not_should_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
         "Success message is presented, but should not be"

    def message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
         "do not message what basket is empty"
