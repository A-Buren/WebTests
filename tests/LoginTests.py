from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
import allure

BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_ERROR = 'Введите логин'
LOGIN_WITHOUT_PASSWORD = 'Введите пароль'


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустой форме авторизации')
def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустой форме авторизации')
def test_login_without_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.input_login()
    LoginPage.click_login()
    assert LoginPage.get_error_text() == LOGIN_WITHOUT_PASSWORD
