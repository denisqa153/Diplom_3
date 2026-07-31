import requests
import allure
from data import BASE_URL


@allure.epic("Лента заказов")
@allure.feature("Функционал ленты заказов")
class TestFeed:

    @allure.title("Тест 1: Клик на заказ открывает всплывающее окно с деталями")
    def test_click_order_opens_modal(self, driver, password_recovery_ui):
        ui = password_recovery_ui
        ui.feed.open_feed(BASE_URL)

        ui.feed.click_first_feed_order()

        assert ui.feed.is_feed_order_modal_visible() is True

    @allure.title("Тест 2: Всплывающее окно заказа закрывается")
    def test_close_order_modal(self, driver, password_recovery_ui):
        ui = password_recovery_ui
        ui.feed.open_feed(BASE_URL)

        ui.feed.click_first_feed_order()
        ui.feed.close_feed_order_modal()

        assert ui.feed.is_feed_order_modal_invisible() is True

    @allure.title("Тест 3: Заказ из «История заказов» отображается на «Лента заказов»")
    def test_user_order_appears_in_feed(self, driver, password_recovery_ui, create_user_success, login_user):
        user = create_user_success

        with allure.step("Создаём заказ через API и проверяем его на ленте"):
            headers = {"Authorization": user["accessToken"]}
            payload = {"ingredients": ["691577430cc94f001a65b859", "691577430cc94f001a65b863"]}
            response = requests.post(f'{BASE_URL}/api/orders', json=payload, headers=headers)
            order_number = response.json()["order"]["number"]

        ui = password_recovery_ui
        ui.feed.open_feed(BASE_URL)

        assert ui.feed.is_order_number_in_feed(order_number), \
            f"Заказ #{order_number} не найден на ленте"

    @allure.title("Тест 4: Номер заказа отображается в истории заказов")
    def test_user_order_appears_in_history(self, driver, password_recovery_ui, create_user_success, login_user):
        user = create_user_success

        with allure.step("Создаём заказ через API"):
            headers = {"Authorization": user["accessToken"]}
            payload = {"ingredients": ["691577430cc94f001a65b859", "691577430cc94f001a65b863"]}
            response = requests.post(f'{BASE_URL}/api/orders', json=payload, headers=headers)
            order_number = response.json()["order"]["number"]

        ui = password_recovery_ui

        with allure.step("Проверяем наличие заказа в истории"):
            ui.feed.open_history_via_ui()
            history_numbers = ui.feed.get_history_order_numbers()
            assert any(str(order_number) in num for num in history_numbers), \
                f"Заказ #{order_number} не найден в истории. Номера: {history_numbers}"

    @allure.title("Тест 5: Счётчик «Выполнено за всё время» увеличивается после нового заказа")
    def test_counter_done_all_increases(self, driver, password_recovery_ui, create_user_success):
        user = create_user_success

        ui = password_recovery_ui
        ui.feed.open_feed(BASE_URL)
        counter_before = ui.feed.get_counter_done_all()

        with allure.step("Создаём заказ через API с авторизацией"):
            headers = {"Authorization": user["accessToken"]}
            payload = {"ingredients": ["691577430cc94f001a65b859", "691577430cc94f001a65b863"]}
            requests.post(f'{BASE_URL}/api/orders', json=payload, headers=headers)

        with allure.step("Перезагружаем страницу и проверяем счётчик"):
            counter_after = ui.feed.reload_and_get_counter_done_all(BASE_URL)

        assert counter_after >= counter_before + 1

    @allure.title("Тест 6: Счётчик «Выполнено за сегодня» увеличивается после нового заказа")
    def test_counter_done_today_increases(self, driver, password_recovery_ui, create_user_success):
        user = create_user_success

        ui = password_recovery_ui
        ui.feed.open_feed(BASE_URL)
        counter_before = ui.feed.get_counter_done_today()

        with allure.step("Создаём заказ через API с авторизацией"):
            headers = {"Authorization": user["accessToken"]}
            payload = {"ingredients": ["691577430cc94f001a65b859", "691577430cc94f001a65b863"]}
            requests.post(f'{BASE_URL}/api/orders', json=payload, headers=headers)

        with allure.step("Перезагружаем страницу и проверяем счётчик"):
            counter_after = ui.feed.reload_and_get_counter_done_today(BASE_URL)

        assert counter_after >= counter_before + 1

    @allure.title("Тест 7: Номер заказа появляется в разделе «В работе»")
    def test_order_appears_in_progress(self, driver, password_recovery_ui, create_user_success, login_user):
        user = create_user_success

        with allure.step("Создаём заказ через API"):
            headers = {"Authorization": user["accessToken"]}
            payload = {"ingredients": ["691577430cc94f001a65b859", "691577430cc94f001a65b863"]}
            response = requests.post(f'{BASE_URL}/api/orders', json=payload, headers=headers)
            order_number = response.json()["order"]["number"]

        ui = password_recovery_ui
        ui.feed.open_feed(BASE_URL)

        with allure.step("Проверяем номер заказа в разделе «В работе»"):
            assert ui.feed.is_order_in_progress(order_number), \
                f"Заказ #{order_number} не найден в разделе «В работе»"
