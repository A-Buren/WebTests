from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    ENTER_TAB = (By.XPATH, '//*[@class="filter_i __active js-login-nav js-login-login"]')
    QR_CODE_TAB = (By.XPATH, '//*[@class="filter_i js-login-nav js-login-qrCode"]')
    LOGIN_WITH_QR_BUTTON = (By.XPATH, '//*[@class="qr-button-label"]')
    FORGOT_LOGIN_BUTTON = (By.CLASS_NAME, 'lp')
    REGISTER_BUTTON = (By.XPATH, '//*[@class="button-pro __sec mb-3x __wide"]')
    VK_LOGIN_BUTTON = (By.XPATH, '//*[@class="i ic social-icon __s __vk_id"]')
    MAIL_LOGIN_BUTTON = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    YANDEX_LOGIN_BUTTON = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.ENTER_TAB)
        self.find_element(LoginPageLocators.QR_CODE_TAB)
        self.find_element(LoginPageLocators.LOGIN_WITH_QR_BUTTON)
        self.find_element(LoginPageLocators.FORGOT_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.REGISTER_BUTTON)
        self.find_element(LoginPageLocators.VK_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.MAIL_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_LOGIN_BUTTON)


    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT).text