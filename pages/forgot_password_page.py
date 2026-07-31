from pages.base_page import BasePage
from locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):

    def open_forgot_password_page(self, base_url):
        self.open_url(f"{base_url}/forgot-password")

    def enter_email(self, email):
        self.fill_input(ForgotPasswordPageLocators.INPUT_EMAIL, email)

    def click_restore_button(self):
        self.wait_for_overlay_to_disappear()
        self.click_element(ForgotPasswordPageLocators.BUTTON_RESTORE)