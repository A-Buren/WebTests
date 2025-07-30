from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, '//*[@id="field_password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    ENTER_TAB = (By.CLASS_NAME, 'filter_i js-login-nav js-login-login __active')
    QR_CODE_TAB = (By.CLASS_NAME, 'filter_i js-login-nav js-login-qrCode')
    LOGIN_WITH_QR_BUTTON = (By.CLASS_NAME, 'qr-button-label')
    FORGOT_LOGIN_BUTTON = (By.CLASS_NAME, 'lp')
    REGISTER_BUTTON = (By.CLASS_NAME, 'button-pro __sec mb-3x __wide')
    VK_LOGIN_BUTTON = (By.CLASS_NAME, 'i ic social-icon __s __vk_id')
    MAIL_LOGIN_BUTTON = (By.CLASS_NAME, 'i ic social-icon __s __mailru')
    YANDEX_LOGIN_BUTTON = (By.CLASS_NAME, 'i ic social-icon __s __yandex')


class LoginPageHelper(BasePage):
    pass

