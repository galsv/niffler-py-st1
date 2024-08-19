import pytest
from niffler_e_2_e_tests_python.model.app import auth_page


def test_successful_authentication(login_page, app_user, browser_quits):
    auth_page.sign_in(*app_user)
    auth_page.login_should_be_successful()


def test_unsuccessful_authentication(login_page, faker, browser_quits):
    auth_page.sign_in(faker.user_name(), faker.password(length=5))
    auth_page.login_should_not_be_successful()
