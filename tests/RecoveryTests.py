import allure
from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelpers

BASE_URL = 'https://ok.ru/'
PASSWORD_TEXT = '2'


@allure.suite('Проверка восстановления пользователя')
@allure.title('Проверка перехода после нескольких неудачных попыток авторизации')
def test_go_to_recovery_after_many_fails(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.input_login()

    for i in range (3):
        LoginPage.input_password(PASSWORD_TEXT)
        LoginPage.click_login()

    LoginPage.click_recovery()
    RecoveryPageHelpers(browser)
