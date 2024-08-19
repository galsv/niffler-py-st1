import pytest
from selene import have
from niffler_e_2_e_tests_python.model.app import start_page


@pytest.mark.parametrize('login_link, register_link',
                         [
                             [
                                 {
                                     'href': '/redirect',
                                     'text': 'Login'
                                 },
                                 {
                                     'href': '/register',
                                     'text': 'Register'
                                 }
                            ]
                         ])
def test_start_page_has_header_and_two_links(start_page_open, frontend_url, auth_url, login_link, register_link):
    start_page.main_header.should(have.exact_text('Welcome to magic journey with Niffler. The coin keeper'))

    start_page.login_link.should(have.exact_text(login_link['text']))
    start_page.login_link.should(have.attribute('href').value(frontend_url + login_link['href']))

    start_page.register_link.should(have.exact_text(register_link['text']))
    start_page.register_link.should(have.attribute('href').value(auth_url + register_link['href']))


@pytest.mark.parametrize('element_link, paragraph_text', [
    (start_page.login_link, 'Please sign in'),
    (start_page.register_link, 'Registration form'),
])
def test_start_pages_link_working(start_page_open, element_link, paragraph_text, browser_quits):
    start_page.link_click(element_link)
    start_page.paragraph_should_have_text(paragraph_text)
