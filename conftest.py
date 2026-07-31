import pytest
import requests
import allure
from data import BASE_URL
from faker import Faker

from helpers import WebdriverFactory
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.profile_page import ProfilePage
from pages.reset_password_page import ResetPasswordPage
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage

fake = Faker()

@pytest.fixture
def create_user_success():
    """Фикстура: регистрирует пользователя и удаляет его после теста."""
    with allure.step("Фикстура: Генерация данных и регистрация нового пользователя"):
        user_data = {
            "email": fake.email(),
            "password": fake.password(length=10),
            "name": fake.first_name()
        }

        response = requests.post(f'{BASE_URL}/api/auth/register', json=user_data)
        response_json = response.json()
        token = response_json.get("accessToken")
        user_data["accessToken"] = token

    yield user_data

    if token:
        with allure.step("Фикстура [Очистка]: Удаление созданного пользователя"):
            requests.delete(f'{BASE_URL}/api/auth/user', headers={"Authorization": token})

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """Кроссбраузерная фикстура создания драйвера."""
    driver_instance = WebdriverFactory.getWebdriver(request.param)
    yield driver_instance
    driver_instance.quit()

@pytest.fixture
def login_user(driver, create_user_success, password_recovery_ui):
    """Фикстура: авторизует пользователя через UI и возвращает данные пользователя."""
    user = create_user_success
    driver.get(f"{BASE_URL}/login")
    password_recovery_ui.login.login(user["email"], user["password"])
    return user

@pytest.fixture
def password_recovery_ui(driver):
    """UI-фикстура возвращает готовые объекты страниц для теста."""
    class Pages:
        login = LoginPage(driver)
        forgot_password = ForgotPasswordPage(driver)
        profile = ProfilePage(driver)
        reset_password = ResetPasswordPage(driver)
        constructor = ConstructorPage(driver)
        feed = FeedPage(driver)

    return Pages
