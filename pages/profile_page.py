from pages.base_page import BasePage
from locators import ProfilePageLocators

class ProfilePage(BasePage):

    def click_header_profile_button(self):
        self.click_element(ProfilePageLocators.HEADER_PROFILE_BUTTON)

    def click_order_history_tab(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY_TAB)

    def click_logout_button(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    def is_profile_tab_active(self):
        tab = self.find_element_with_wait(ProfilePageLocators.PROFILE_TAB)
        return "Account_link_active" in tab.get_attribute("class")

    def is_order_history_tab_active(self):
        tab = self.find_element_with_wait(ProfilePageLocators.ORDER_HISTORY_TAB)
        return "Account_link_active" in tab.get_attribute("class")
