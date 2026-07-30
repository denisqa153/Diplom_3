import allure
from data import BASE_URL

@allure.epic("Главная страница")
@allure.feature("Конструктор и функционал заказов")
class TestConstructor:

    @allure.title("Тест 1: Переход по клику на «Конструктор»")
    def test_navigate_to_constructor(self, driver, password_recovery_ui):
        ui = password_recovery_ui
        ui.constructor.open_feed(BASE_URL)

        ui.constructor.click_header_constructor()
        assert ui.constructor.is_constructor_title_visible() is True

    @allure.title("Тест 2: Переход по клику на «Лента заказов»")
    def test_navigate_to_feed(self, driver, password_recovery_ui):
        ui = password_recovery_ui
        ui.constructor.open(BASE_URL)

        ui.constructor.click_header_feed()
        assert ui.constructor.is_feed_title_visible() is True

    @allure.title("Тест 3: Клик на ингредиент открывает всплывающее окно с деталями")
    def test_open_ingredient_modal(self, driver, password_recovery_ui):
        ui = password_recovery_ui
        ui.constructor.open(BASE_URL)

        ui.constructor.click_first_ingredient()
        assert ui.constructor.is_modal_details_visible() is True

    @allure.title("Тест 4: Всплывающее окно закрывается кликом по крестику")
    def test_close_ingredient_modal(self, driver, password_recovery_ui):
        ui = password_recovery_ui
        ui.constructor.open(BASE_URL)

        ui.constructor.click_first_ingredient()
        ui.constructor.click_close_modal()

    @allure.title("Тест 5: Добавление ингредиента в заказ увеличивает каунтер")
    def test_ingredient_counter_increases(self, driver, password_recovery_ui):
        ui = password_recovery_ui
        ui.constructor.open(BASE_URL)

        ui.constructor.drag_and_drop_ingredient_to_basket()

        new_count = ui.constructor.get_ingredient_counter_value()
        assert new_count == 2

    @allure.title("Тест 6: Залогиненный пользователь может оформить заказ")
    def test_logged_user_can_create_order(self, driver, password_recovery_ui, create_user_success, login_user):
        ui = password_recovery_ui
        ui.constructor.open(BASE_URL)
        assert ui.constructor.is_constructor_title_visible() is True

        ui.constructor.drag_and_drop_ingredient_to_basket()
        ui.constructor.click_create_order()

        assert ui.constructor.is_order_submitted_modal_visible() is True