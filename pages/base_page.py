from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import OVERLAY_LOCATOR

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator, time=5):
        return WebDriverWait(self.driver, timeout=time).until(
            EC.presence_of_element_located(locator),
            message=f"Не удалось дождаться элемента по локатору: {locator}"
        )

    def click_element(self, locator):
        element = self.find_element_with_wait(locator)
        WebDriverWait(self.driver, timeout=5).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не стал кликабельным: {locator}"
        )
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    def fill_input(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_overlay_to_disappear(self, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(OVERLAY_LOCATOR),
            message="Модальный оверлей не исчез за отведённое время"
        )
