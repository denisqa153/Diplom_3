from selenium.webdriver.common.by import By

OVERLAY_LOCATOR = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay')]")


class LoginPageLocators:
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")


class ForgotPasswordPageLocators:
    INPUT_EMAIL = (By.NAME, "name")
    BUTTON_RESTORE = (By.XPATH, ".//button[text()='Восстановить']")


class ResetPasswordPageLocators:
    INPUT_PASSWORD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    INPUT_CODE = (By.XPATH, ".//label[text()='Введите код из письма']/following-sibling::input")
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")
    EYE_BUTTON = (By.XPATH, ".//div[contains(@class, 'input_type_password')]//div[contains(@class, 'input__icon')]")
    PASSWORD_FIELD_CONTAINER = (By.XPATH, ".//div[contains(@class, 'input_type_password')]")

class ProfilePageLocators:
    HEADER_PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    PROFILE_TAB = (By.XPATH, ".//a[text()='Профиль']")
    ORDER_HISTORY_TAB = (By.XPATH, ".//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

class ConstructorPageLocators:
    HEADER_CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    HEADER_FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")
    FEED_TITLE = (By.XPATH, ".//h1[text()='Лента заказов']")
    FIRST_INGREDIENT = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]//p[contains(@class, 'counter_counter__num')]")
    BURGER_CONSTRUCTOR_SECTION = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")
    MODAL_DETAILS = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    ORDER_SUBMITTED_MODAL = (By.XPATH, ".//p[contains(text(), 'идентификатор заказа')]")

class FeedPageLocators:
    FEED_TITLE = (By.XPATH, ".//h1[text()='Лента заказов']")
    FEED_ORDER_CARD = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li")
    FEED_ORDER_NUMBER = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li//p[contains(@class, 'digits-default')]")
    MODAL_ORDER_NUMBER = (By.XPATH, ".//section[contains(@class, 'Modal')]//h2[contains(@class, 'title')]")
    MODAL_ORDER_STATUS = (By.XPATH, ".//section[contains(@class, 'Modal')]//p[contains(text(), 'Выполнен')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")
    MODAL_VISIBLE = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")
    COUNTER_DONE_ALL = (By.XPATH, ".//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    COUNTER_DONE_TODAY = (By.XPATH, ".//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    IN_PROGRESS_LIST = (By.XPATH, ".//ul[not(contains(@class, 'Ready')) and contains(@class, 'OrderFeed_orderList')]/li")
    HISTORY_ORDER_CARD = (By.XPATH, ".//a[contains(@class, 'OrderHistory_link')]")
    HISTORY_ORDER_NUMBER = (By.XPATH, ".//a[contains(@class, 'OrderHistory_link')]//p[contains(@class, 'digits-default')]")
