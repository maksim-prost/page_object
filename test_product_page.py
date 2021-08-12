from .pages.login_page import LoginPage
from .pages.product_page import PageProduct
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.locators import AddBasketPageLocators
import pytest
import time


@pytest.mark.parametrize("link", 
[f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" for i in range(10) 
            if i != 7] + [ pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail) ])
def test_guest_can_go_to_basket_page(browser, link):
    page = PageProduct (browser, link) 
    page.open() 
    page.add_product_to_basket()
   
@pytest.mark.xfail 
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageProduct (browser, link) 
    page.open() 
    page.add_product_to_basket()
    page.cant_see_success_message_after_adding_product_to_basket()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageProduct (browser, link) 
    page.open() 
    page.cant_see_success_message()
 

@pytest.mark.xfail 
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageProduct (browser, link) 
    page.open() 
    page.add_product_to_basket()
    page.message_disappeared_after_adding_product_to_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageProduct(browser, link)
    page.open()
    page.should_be_login_link()

def can_add_product_to_basket(browser, link):
    page = PageProduct(browser, link)
    page.open()
    page.add_product_to_basket() 

@pytest.mark.basket
class TestUserAddToBasketFromProductPaget():
    @pytest.fixture(scope="class", autouse=True)
    def setup(self,browser):
        page = MainPage(browser)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(*[f'{s}@gmail.com' for s in str(time.time()).split('.')])
        login_page.should_be_authorized_user()

    def guest_cant_see_product_in_basket_opened(self,browser, page):
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.not_should_items()
        basket_page.message_empty_basket()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser)
        self.guest_cant_see_product_in_basket_opened(browser, page)
        
    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = PageProduct(browser, link)
        self.guest_cant_see_product_in_basket_opened(browser, page)
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/studyguide-for-counter-hack-reloaded_205/'
        can_add_product_to_basket(browser, link)

@pytest.mark.need_review
@pytest.mark.parametrize("link", ['http://selenium1py.pythonanywhere.com/ru/catalogue/studyguide-for-counter-hack-reloaded_205/'])
def test_guest_can_add_product_to_basket(browser, link):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/studyguide-for-counter-hack-reloaded_205/'
    can_add_product_to_basket(browser, link)


@pytest.mark.need_review
@pytest.mark.parametrize("link", ['http://selenium1py.pythonanywhere.com/ru/catalogue/studyguide-for-counter-hack-reloaded_205/'])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser,link):
    page = PageProduct(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.not_should_items()
    basket_page.message_empty_basket()

@pytest.mark.need_review
@pytest.mark.parametrize("link", ['http://selenium1py.pythonanywhere.com/ru/catalogue/studyguide-for-counter-hack-reloaded_205/'])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = PageProduct(browser, link)
    page.open()
    page.should_be_login_link()
    login_page= LoginPage(browser, link)
    login_page.should_be_login_link()
