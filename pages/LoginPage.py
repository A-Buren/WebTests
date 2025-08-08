from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure

from pages.RecoveryPage import RecoveryPageHelpers, RecoveryPageLocators


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    ENTER_TAB = (By.XPATH, '//*[@class="filter_i __active js-login-nav js-login-login"]')
    QR_CODE_TAB = (By.XPATH, '//*[@class="filter_i js-login-nav js-login-qrCode"]')
    LOGIN_WITH_QR_BUTTON = (By.XPATH, '//*[@class="qr-button-label"]')
    RESTORE_LINK = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTER_BUTTON = (By.XPATH, '//*[@class="button-pro __sec mb-3x __wide"]')
    VK_LOGIN_BUTTON = (By.XPATH, '//*[@class="i ic social-icon __s __vk_id"]')
    MAIL_LOGIN_BUTTON = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    YANDEX_LOGIN_BUTTON = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')
    GO_BACK_BUTTON = (By.XPATH, '//*[@data-l="t,cancel"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="external-oauth-login-help portlet_f"]')
    PROFILE_RECOVERY_BUTTON = (By.NAME, 'st.go_to_recovery')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.ENTER_TAB)
        self.find_element(LoginPageLocators.QR_CODE_TAB)
        self.find_element(LoginPageLocators.LOGIN_WITH_QR_BUTTON)
        self.find_element(LoginPageLocators.RESTORE_LINK)
        self.find_element(LoginPageLocators.REGISTER_BUTTON)
        self.find_element(LoginPageLocators.VK_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.MAIL_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_LOGIN_BUTTON)


    @allure.step('Нажимаем на кнопку "Войти в Одноклассники"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Заполняем поле "Логин"')
    def input_login(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys("абырвалг1@mail.ru")
        self.attach_screenshot()

    @allure.step('Заполняем поле "Пароль"')
    def input_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Переходим к восстанавлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.PROFILE_RECOVERY_BUTTON).click()

    @allure.step('Переходим к регистрации')
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTER_BUTTON).click()