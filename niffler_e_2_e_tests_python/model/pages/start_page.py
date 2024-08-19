from selene import browser, have
from selene.core.entity import Element


class StartPage:
    def __init__(self):
        self.main_header = browser.element('.main__header')
        self.links = browser.all('.main__link')
        self.login_link = self.links.first
        self.register_link = self.links.second

    @staticmethod
    def link_click(element: Element):
        element.click()

    @staticmethod
    def paragraph_should_have_text(text: str):
        browser.element('.form__paragraph').should(have.exact_text(text))
