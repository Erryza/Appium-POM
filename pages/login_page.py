from locators.login_locator import LoginLocator
from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def option_btn(self):
        self.click_element(LoginLocator.option_login_btn)

    def input_email(self, email):
        self.enter_el_text(LoginLocator.input_email, email)

    def input_password(self, password):
        self.enter_el_text(LoginLocator.input_password, password)

    def click_btn(self):
        self.click_element(LoginLocator.login_btn)
