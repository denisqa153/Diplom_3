import allure
from data import BASE_URL


@allure.epic("Личный Кабинет")
@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Тест 1: Переход на страницу восстановления пароля по кнопке")
    def test_success_to_forgot_password_page(self, driver, password_recovery_ui):
        password_recovery_ui.login.open_login(BASE_URL)

        password_recovery_ui.login.click_forgot_password()

        with allure.step("Проверить, что URL изменился на /forgot-password"):
            assert "/forgot-password" in password_recovery_ui.login.get_current_url()

    @allure.title("Тест 2: Ввод почты зарегистрированного пользователя и клик 'Восстановить'")
    def test_submit_forgot_password_form(self, driver, password_recovery_ui, create_user_success):
        user_email = create_user_success["email"]

        password_recovery_ui.forgot_password.open_forgot_password_page(BASE_URL)

        password_recovery_ui.forgot_password.enter_email(user_email)
        password_recovery_ui.forgot_password.click_restore_button()

        with allure.step("Проверить переход на страницу ввода нового пароля /reset-password"):
            assert password_recovery_ui.forgot_password.wait_for_url_contains("/reset-password"), \
                "Не выполнен переход на /reset-password"