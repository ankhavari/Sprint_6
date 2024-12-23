import allure
from pages.base_page import BasePage
from utils.locators import BasePageLocators
from utils.locators import HomePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    @allure.step('Принять куки')
    def click_cookie_confirm(self):
        return self.find_element(BasePageLocators.COOKIE_ACCEPT_BUTTON).click()

    @allure.step('Нажать кнопку Заказать в верхней части страницы')
    def click_header_order_button(self):
        return self.find_element(HomePageLocators.HEADER_ORDER_BUTTON).click()

    @allure.step('Нажать кнопку Заказать в нижней части страницы')
    def click_finish_order_button(self):
        return self.find_element(HomePageLocators.FINISH_ORDER_BUTTON).click()

    @allure.step('Нажать на вопрос')
    def click_faq_question(self, question_number: int):
        elems = self.find_elements(HomePageLocators.FAQ_BUTTON, 10)
        return elems[question_number].click()

    @allure.step('Переключиться на открывшуюся вкладку браузера')
    def switch_window(self, window_number: int=1):
        return self.driver.switch_to.window(self.driver.window_handles[window_number])

    def wait_url_until_not_about_blank(self, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))

    @allure.step('Нажать на лого Яндекса')
    def click_yandex_logo(self):
        return self.find_element(BasePageLocators.YANDEX_LOGO).click()

