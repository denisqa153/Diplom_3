import allure
from pages.base_page import BasePage
from locators import ResetPasswordPageLocators

class ResetPasswordPage(BasePage):

    @allure.step("Кликнуть по иконке показа/скрытия пароля ('глазику')")
    def click_eye_button(self):
        self.click_element(ResetPasswordPageLocators.EYE_BUTTON)

    @allure.step("Получить значение атрибута class у контейнера поля пароля")
    def get_password_container_class(self):
        container = self.find_element_with_wait(ResetPasswordPageLocators.PASSWORD_FIELD_CONTAINER)
        return container.get_attribute("class")
