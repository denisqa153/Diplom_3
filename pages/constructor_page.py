from pages.base_page import BasePage
from locators import ConstructorPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConstructorPage(BasePage):

    def click_header_constructor(self):
        self.wait_for_overlay_to_disappear()
        self.click_element(ConstructorPageLocators.HEADER_CONSTRUCTOR_BUTTON)

    def click_header_feed(self):
        self.wait_for_overlay_to_disappear()
        self.click_element(ConstructorPageLocators.HEADER_FEED_BUTTON)

    def click_first_ingredient(self):
        self.click_element(ConstructorPageLocators.FIRST_INGREDIENT)

    def click_close_modal(self):
        self.click_element(ConstructorPageLocators.MODAL_CLOSE_BUTTON)
        WebDriverWait(self.driver, timeout=5).until(
            EC.invisibility_of_element_located(ConstructorPageLocators.MODAL_DETAILS),
            message="Модальное окно деталей ингредиента не закрылось"
        )

    def is_constructor_title_visible(self):
        return self.find_element_with_wait(ConstructorPageLocators.CONSTRUCTOR_TITLE).is_displayed()

    def is_feed_title_visible(self):
        return self.find_element_with_wait(ConstructorPageLocators.FEED_TITLE).is_displayed()

    def is_modal_details_visible(self):
        return self.find_element_with_wait(ConstructorPageLocators.MODAL_DETAILS).is_displayed()

    def drag_and_drop_ingredient_to_basket(self):
        source = self.find_element_with_wait(ConstructorPageLocators.FIRST_INGREDIENT)
        target = self.find_element_with_wait(ConstructorPageLocators.BURGER_CONSTRUCTOR_SECTION)

        # Пробуем два метода drag-and-drop:
        # 1) Ручная цепочка ActionChains — работает в Chrome.
        # 2) JS-fallback через нативный DragEvent — для Firefox/Geckodriver,
        #    где ActionChains не триггерит HTML5 DnD-события для React DnD.
        ActionChains(self.driver).click_and_hold(source).pause(0.2).move_to_element(target).pause(0.2).release(target).perform()

        if self.get_ingredient_counter_value() == 0:
            self._js_drag_and_drop(source, target)

        # React DnD обрабатывает drop асинхронно через setState —
        # ждём обновления счётчика.
        WebDriverWait(self.driver, timeout=5).until(
            lambda d: self.get_ingredient_counter_value() > 0,
            message="Счётчик ингредиента не обновился после drag-and-drop"
        )

    def _js_drag_and_drop(self, source, target):
        js_drag = """
            function simulateDragDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();

                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true, cancelable: true, dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);

                var dragEnterEvent = new DragEvent('dragenter', {
                    bubbles: true, cancelable: true, dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dragEnterEvent);

                var dragOverEvent = new DragEvent('dragover', {
                    bubbles: true, cancelable: true, dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dragOverEvent);

                var dropEvent = new DragEvent('drop', {
                    bubbles: true, cancelable: true, dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dropEvent);

                var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true, cancelable: true, dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragEndEvent);
            }
            simulateDragDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(js_drag, source, target)

    def get_ingredient_counter_value(self):
        try:
            element = self.find_element_with_wait(ConstructorPageLocators.INGREDIENT_COUNTER, time=2)
            return int(element.text)
        except (NoSuchElementException, ValueError):
            return 0

    def click_create_order(self):
        self.click_element(ConstructorPageLocators.CREATE_ORDER_BUTTON)

    def is_order_submitted_modal_visible(self):
        WebDriverWait(self.driver, timeout=15).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ORDER_SUBMITTED_MODAL),
            message="Модальное окно заказа не появилось"
        )
        return True
    def open(self, base_url):
        self.driver.get(base_url)
        return self

    def open_feed(self, base_url):
        self.driver.get(f"{base_url}/feed")
        return self
