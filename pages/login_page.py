from pages.base_page import BasePage
from locators import LoginPageLocators, ConstructorPageLocators

class LoginPage(BasePage):

    def open_login_page(self, base_url):
        self.open_url(f"{base_url}/login")

    def open_login(self, base_url):
        self.open_url(f"{base_url}/login")
        return self

    def click_forgot_password(self):
        self.wait_for_overlay_to_disappear()
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def login(self, email, password):
        self.fill_input(LoginPageLocators.EMAIL_INPUT, email)
        self.fill_input(LoginPageLocators.PASSWORD_INPUT, password)
        self.wait_for_overlay_to_disappear()
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_visibility(ConstructorPageLocators.CONSTRUCTOR_TITLE, time=10)