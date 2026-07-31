import allure


@allure.epic("Личный Кабинет")
@allure.feature("Управление профилем")
class TestProfile:

    @allure.title("Тест 1: Переход по клику на «Личный кабинет»")
    def test_navigate_to_profile_page(self, driver, password_recovery_ui, create_user_success, login_user):
        ui = password_recovery_ui

        with allure.step("Кликнуть на кнопку 'Личный кабинет' в шапке"):
            ui.profile.click_header_profile_button()

        with allure.step("Проверить переход в личный кабинет"):
            assert ui.profile.is_profile_tab_active() is True

    @allure.title("Тест 2: Переход в раздел «История заказов»")
    def test_navigate_to_order_history(self, driver, password_recovery_ui, create_user_success, login_user):
        ui = password_recovery_ui

        with allure.step("Перейти в личный кабинет и нажать 'История заказов'"):
            ui.profile.click_header_profile_button()
            ui.profile.click_order_history_tab()

        with allure.step("Проверить активацию вкладки 'История заказов'"):
            assert ui.profile.is_order_history_tab_active() is True

    @allure.title("Тест 3: Выход из аккаунта")
    def test_logout_from_account(self, driver, password_recovery_ui, create_user_success, login_user):
        ui = password_recovery_ui

        with allure.step("Перейти в личный кабинет и нажать 'Выход'"):
            ui.profile.click_header_profile_button()
            ui.profile.click_logout_button()

        with allure.step("Проверить редирект на страницу логина после выхода"):
            assert ui.profile.wait_for_url_contains("/login")
