from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelper
from pages.HelpPage import HelpPageLocators
from  pages.AdvertisementCabinetHelp import AdvertisementCabinetHelpHelpers
import allure

BASE_URL = 'https://ok.ru/help'


def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelpHelpers(browser)
