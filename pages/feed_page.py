import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import FeedPageLocators, ProfilePageLocators


class FeedPage(BasePage):

    def open_feed(self, base_url):
        self.driver.get(f"{base_url}/feed")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(FeedPageLocators.FEED_TITLE),
            message="Страница ленты заказов не загрузилась"
        )

    def is_feed_title_visible(self):
        return self.find_element_with_wait(FeedPageLocators.FEED_TITLE).is_displayed()

    def click_first_feed_order(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(FeedPageLocators.FEED_ORDER_CARD),
            message="Карточка заказа не кликабельна"
        )
        element.click()

    def is_feed_order_modal_visible(self):
        WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(FeedPageLocators.MODAL_VISIBLE),
            message="Модалка заказа не появилась"
        )
        return True

    def close_feed_order_modal(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(FeedPageLocators.MODAL_CLOSE_BUTTON),
            message="Кнопка закрытия модалки не кликабельна"
        )
        element.click()
        WebDriverWait(self.driver, timeout=5).until(
            EC.invisibility_of_element_located(FeedPageLocators.MODAL_VISIBLE),
            message="Модалка заказа не закрылась"
        )

    def get_counter_done_all(self):
        return int(self.find_element_with_wait(FeedPageLocators.COUNTER_DONE_ALL).text)

    def get_counter_done_today(self):
        return int(self.find_element_with_wait(FeedPageLocators.COUNTER_DONE_TODAY).text)

    def reload_and_get_counter_done_all(self, base_url, attempts=7, delay=3):
        for _ in range(attempts):
            self.open_feed(base_url)
            time.sleep(delay)
        return self.get_counter_done_all()

    def reload_and_get_counter_done_today(self, base_url, attempts=7, delay=3):
        for _ in range(attempts):
            self.open_feed(base_url)
            time.sleep(delay)
        return self.get_counter_done_today()

    def get_in_progress_orders(self):
        elements = self.find_elements_with_wait(FeedPageLocators.IN_PROGRESS_LIST)
        return [el.text for el in elements]

    def is_order_in_progress(self, order_number):
        orders = self.get_in_progress_orders()
        return any(str(order_number) in order for order in orders)

    def is_order_number_in_feed(self, order_number):
        formatted = str(order_number).zfill(6)
        elements = self.driver.find_elements(*FeedPageLocators.FEED_ORDER_NUMBER)
        for el in elements:
            try:
                if formatted in el.text:
                    return True
            except Exception:
                continue
        return False

    def open_history_via_ui(self):
        self.click_element(ProfilePageLocators.HEADER_PROFILE_BUTTON)
        WebDriverWait(self.driver, 5).until(EC.url_contains("/account/profile"))
        self.click_element(ProfilePageLocators.ORDER_HISTORY_TAB)
        WebDriverWait(self.driver, 5).until(EC.url_contains("/account/order-history"))

    def get_history_order_numbers(self):
        elements = self.find_elements_with_wait(FeedPageLocators.HISTORY_ORDER_NUMBER)
        result = []
        for el in elements:
            try:
                result.append(el.text)
            except Exception:
                continue
        return result

    def find_elements_with_wait(self, locator, time=5):
        WebDriverWait(self.driver, timeout=time).until(
            EC.presence_of_element_located(locator),
            message=f"Не удалось дождаться элементов по локатору: {locator}"
        )
        return self.driver.find_elements(*locator)
