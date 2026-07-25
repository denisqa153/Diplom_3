import allure
from data import BASE_URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.epic("Личный Кабинет")
@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Тест 1: Переход на страницу восстановления пароля по кнопке")
    def test_success_to_forgot_password_page(self, driver, password_recovery_ui):
        with allure.step("Открыть страницу авторизации"):
            driver.get(f"{BASE_URL}/login")

        password_recovery_ui.login.click_forgot_password()

        with allure.step("Проверить, что URL изменился на /forgot-password"):
            assert "/forgot-password" in driver.current_url

    @allure.title("Тест 2: Ввод почты зарегистрированного пользователя и клик 'Восстановить'")
    def test_submit_forgot_password_form(self, driver, password_recovery_ui, create_user_success):
        user_email = create_user_success["email"]

        with allure.step("Открыть страницу восстановления пароля"):
            driver.get(f"{BASE_URL}/forgot-password")

        password_recovery_ui.forgot_password.enter_email(user_email)
        password_recovery_ui.forgot_password.click_restore_button()

        with allure.step("Проверить переход на страницу ввода нового пароля /reset-password"):
            WebDriverWait(driver, 5).until(EC.url_contains("/reset-password"))
            assert "/reset-password" in driver.current_url
