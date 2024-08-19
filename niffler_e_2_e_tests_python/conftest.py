import os

import pytest
from dotenv import load_dotenv
from selene import browser
from faker import Faker
from niffler_e_2_e_tests_python.model.app import auth_page
from niffler_e_2_e_tests_python.api.user import User


@pytest.fixture(scope="session")
def envs():
    load_dotenv()


@pytest.fixture(scope="session")
def frontend_url(envs):
    return os.getenv("FRONTEND_URL")


@pytest.fixture(scope="session")
def gateway_url(envs):
    return os.getenv("GATEWAY_URL")


@pytest.fixture(scope="session")
def auth_url(envs):
    return os.getenv("AUTH_URL")


@pytest.fixture(scope="session")
def app_user(envs):
    user_api = User()
    user, password = os.getenv("TEST_USERNAME"), os.getenv("TEST_PASSWORD")
    user_api.register(user, password)
    return user, password


@pytest.fixture(scope="session")
def browser_management():
    browser.config.timeout = 15
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture(scope="session")
def auth_completed(browser_management, frontend_url, app_user):
    browser.open(frontend_url)
    browser.element('a[href*=redirect]').click()
    username, password = app_user
    auth_page.sign_in(username, password)

    return browser.driver.execute_script('return window.sessionStorage.getItem("id_token")')


@pytest.fixture()
def browser_quits():
    yield
    browser.quit()


@pytest.fixture()
def start_page_open(browser_management, frontend_url):
    browser.open(frontend_url)


@pytest.fixture()
def login_page(browser_management, frontend_url):
    browser.open(frontend_url)
    browser.element('a[href*=redirect]').click()


@pytest.fixture()
def main_page(auth_completed, frontend_url):
    browser.open(frontend_url)

@pytest.fixture()
def faker():
    return Faker()