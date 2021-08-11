from .pages.product_page import PageProduct
from .pages.locators import AddBasketPageLocators
import pytest

# @pytest.mark.parametrize("link", 
# [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" for i in range(10) 
#             if i != 7] + [ pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail) ])
# def test_guest_can_go_to_basket_page(browser, link):
#     page = PageProduct (browser, link) 
#     page.open() 
#     page.add_product_to_basket()
   
@pytest.mark.xfail 
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageProduct (browser, link) 
    page.open() 
    page.add_product_to_basket()
    assert page.is_not_element_present(*AddBasketPageLocators.MESSAGE_SUCCES), \
         "Success message is presented, but should not be"

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageProduct (browser, link) 
    page.open() 
    assert page.is_not_element_present(*AddBasketPageLocators.MESSAGE_SUCCES), \
         "Success message is presented, but should not be"

@pytest.mark.xfail 
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageProduct (browser, link) 
    page.open() 
    page.add_product_to_basket()
    assert page.is_disappeared(*AddBasketPageLocators.MESSAGE_SUCCES), \
         "Success message is presented, but should not be"