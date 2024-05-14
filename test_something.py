from selene import browser, have, command


def test_demoqa_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Doe')
    browser.element('#userEmail').type('test@mail.com')

