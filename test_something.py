from selene import browser, have, command
import json
import allure
from allure_commons.types import Severity
from allure import attachment_type




@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Sarvar")
@allure.feature("Задачи в репозиторий")
@allure.story("Авторизованный пользователь может создать задачу и репозитории")
@allure.link("https://demoqa.com", name="Testing")

def test_demoqa_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Doe')
    browser.element('#userEmail').type('test@mail.com')

