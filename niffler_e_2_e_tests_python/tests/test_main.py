from selene import browser, have


def test_spending_title_exists(main_page, browser_quits):
    browser.element('.main-content').should(have.text('History of spendings'))
