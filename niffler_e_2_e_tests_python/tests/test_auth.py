import pytest
from niffler_e_2_e_tests_python.model.app import auth_page


def test_successful_authentication(login_page, app_user, browser_quits):
    auth_page.sign_in(*app_user)
    auth_page.login_should_be_successful()

@pytest.mark.parametrize('username, password', [('username', 'password')])
def test_unsuccessful_authentication(login_page, username, password, browser_quits):
    auth_page.sign_in(username, password)
    auth_page.login_should_not_be_successful()
