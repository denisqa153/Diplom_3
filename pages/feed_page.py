import time
from pages.base_page import BasePage
from locators import FeedPageLocators, ProfilePageLocators


class FeedPage(BasePage):

    def open_feed(self, base_url):
        self.open_url(f"{base_url}/feed")
        self.wait_for_visibility(FeedPageLocators.FEED_TITLE, time=10)

    def is_feed_title_visible(self):
        return self.find_element_with_wait(FeedPageLocators.FEED_TITLE).is_displayed()

    def click_first_feed_order(self):
        element = self.wait_for_clickable(FeedPageLocators.FEED_ORDER_CARD, time=10)
        element.click()

    def is_feed_order_modal_visible(self):
        self.wait_for_visibility(FeedPageLocators.MODAL_VISIBLE, time=10)
        return True

    def is_feed_order_modal_invisible(self):
        try:
            self.wait_for_invisibility(FeedPageLocators.MODAL_VISIBLE, time=5)
            return True
        except Exception:
            return False

    def close_feed_order_modal(self):
        self.click_element(FeedPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_invisibility(FeedPageLocators.MODAL_VISIBLE)

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
        elements = self.find_elements_with_wait(FeedPageLocators.FEED_ORDER_NUMBER)
        for el in elements:
            try:
                if formatted in el.text:
                    return True
            except Exception:
                continue
        return False

    def open_history_via_ui(self):
        self.click_element(ProfilePageLocators.HEADER_PROFILE_BUTTON)
        self.wait_for_url_contains("/account/profile")
        self.click_element(ProfilePageLocators.ORDER_HISTORY_TAB)
        self.wait_for_url_contains("/account/order-history")

    def get_history_order_numbers(self):
        elements = self.find_elements_with_wait(FeedPageLocators.HISTORY_ORDER_NUMBER)
        result = []
        for el in elements:
            try:
                result.append(el.text)
            except Exception:
                continue
        return result