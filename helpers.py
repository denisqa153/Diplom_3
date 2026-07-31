from selenium import webdriver

class WebdriverFactory:
    @staticmethod
    def getWebdriver(browser_name):
        if browser_name == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--start-maximized")
            return webdriver.Chrome(options=chrome_options)

        elif browser_name == "firefox":
            driver = webdriver.Firefox()
            driver.maximize_window()
            return driver

        else:
            raise ValueError(f"Неподдерживаемый браузер: '{browser_name}'. Допустимые значения: 'chrome', 'firefox'.")
