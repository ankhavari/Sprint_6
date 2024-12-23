import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.constants import Urls
from utils.locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Перейти на сайт')
    def go_to_site(self, url=None):
        if url is None:
            url = Urls.MAIN_PAGE
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    @allure.step('Получить текущий url')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Нажать на лого Самоката')
    def click_samokat_logo(self):
        return self.find_element(BasePageLocators.SAMOKAT_LOGO).click()