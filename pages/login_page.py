from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import LoginPageLocators, ConstructorPageLocators

class LoginPage(BasePage):

    def open_login_page(self, base_url):
        self.driver.get(f"{base_url}/login")

    def open_login(self, base_url):
        self.driver.get(f"{base_url}/login")
        return self

    def click_forgot_password(self):
        self.wait_for_overlay_to_disappear()
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def login(self, email, password):
        self.fill_input(LoginPageLocators.EMAIL_INPUT, email)
        self.fill_input(LoginPageLocators.PASSWORD_INPUT, password)
        self.wait_for_overlay_to_disappear()
        button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON),
            message="Кнопка 'Войти' не кликабельна"
        )
        button.click()
        WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.CONSTRUCTOR_TITLE),
            message="Не произошёл редирект после логина"
        )