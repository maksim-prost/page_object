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
    
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        input_email.send_keys(email)
        input_password1 = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD1)
        input_password2 = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD2)
        input_password1.send_keys(password)
        input_password2.send_keys(password)
        link_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        link_register.click()