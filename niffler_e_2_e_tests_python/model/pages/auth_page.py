from selene import browser, have, be


class AuthPage:
    def __init__(self):
        self.username = browser.element('input[name=username]')
        self.password = browser.element('input[name=password]')
        self.submit_btn = browser.element('button[type=submit]')

    def sign_in(self, login: str, password: str):
        self.username.set_value(login)
        self.password.set_value(password)
        self.submit_btn.click()

    @staticmethod
    def login_should_be_successful():
        browser.element('.button-icon_type_logout').should(be.in_dom)

    @staticmethod
    def login_should_not_be_successful():
        browser.element('.form__error').should(have.exact_text('Неверные учетные данные пользователя'))
