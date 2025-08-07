from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure
import random


class RegistrationPageLocators:
    PHONE_FIELD = (By.XPATH, '//div[@data-l="t,phone"]')
    COUNTRY_LIST = (By.XPATH, '//div[@data-l="t,country"]')
    COUNTRY_ITEM = (By.XPATH, '//div[@class="country-select_code"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@data-l="t,submit"]')
    AGREEMENT_BUTTON = (By.XPATH, '//*[@data-l="t,agreement"]')
    PRIVACY_BUTTON = (By.XPATH, '//*[@data-l="t,privacy"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@data-l="t,support"]')


class RegistrationPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(RegistrationPageLocators.PHONE_FIELD)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST)
        self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)
        self.find_element(RegistrationPageLocators.AGREEMENT_BUTTON)
        self.find_element(RegistrationPageLocators.PRIVACY_BUTTON)
        self.find_element(RegistrationPageLocators.SUPPORT_BUTTON)

    def select_random_country(self):
        with allure.step('Выбираем случайное число из массива доступных стран'):
            random_number = random.randint(0, 212)
        with allure.step('Нажимаем на выпадающий список "Страна/регион"'):
            self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
            self.attach_screenshot()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        country_code = country_items[random_number].get_attribute('text')
        with allure.step('Нажимаем на случайный элемент из раскрывшегося списка стран'):
            country_items[random_number].click()
            self.attach_screenshot()
        return country_code

    def get_phone_field_value(self):
        return self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute('value')
