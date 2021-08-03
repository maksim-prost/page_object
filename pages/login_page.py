from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        # self.open()current_url
        self.open()
        assert "/login" in self.browser.current_url, "login is absent in current url"
        
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "Login form is not presented"
           # реализуйте проверку, что есть форма логина
       
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTER), "Login form is not presented"
        # реализуйте проверку, что есть форма регистрации на странице
