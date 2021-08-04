from .pages.product_page import PageProduct
import pytest


@pytest.mark.parametrize("link", 
[f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" for i in range(10) 
            if i != 7] + [ pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail) ])
def test_guest_can_go_to_basket_page(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = PageProduct (browser, link) 
    page.open() 
    page.add_product_to_basket()
    # page.solve_quiz_and_get_code()
