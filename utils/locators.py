from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePageLocators:
    YANDEX_LOGO = (By.XPATH, ".//img[@alt='Yandex']")
    SAMOKAT_LOGO = (By.XPATH, ".//img[@alt='Scooter']")
    COOKIE_ACCEPT_BUTTON = (By.XPATH, ".//button[@id='rcc-confirm-button']")

class HomePageLocators:
    HEADER_ORDER_BUTTON = (By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']")
    FINISH_ORDER_BUTTON = (By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']")
    FAQ_BUTTON = (By.XPATH, ".//div[@class='accordion__button']")
    FAQ_ANSWER = (By.CSS_SELECTOR, ".accordion__panel > p")

    @staticmethod
    def FAQ_QUESTION_BUTTON(question_number):
        return [By.XPATH, f".//div[@class='accordion__button' and @id='accordion__heading-{question_number}']"]

    @staticmethod
    def FAQ_ANSWER_BUTTON(answer_number):
        return [By.XPATH, f'.//div[@class="accordion__panel" and @id="accordion__panel-{answer_number}"]/p']

class OrderPageLocator:
    NAME_INPUT = (By.XPATH, ".//input[contains(@placeholder,'Имя')]")
    SURNAME_INPUT = (By.XPATH, ".//input[contains(@placeholder,'Фамилия')]")
    ADDRESS_INPUT = (By.XPATH, ".//input[contains(@placeholder,'Адрес')]")
    METRO_STATION_INPUT = (By.XPATH, ".//input[contains(@placeholder,'Станция метро')]")
    PHONE_NUMBER_INPUT = (By.XPATH, ".//input[contains(@placeholder,'Телефон')]")
    NEXT_BUTTON = (By.XPATH, ".//button[contains(text(),'Далее')]")
    DATE_INPUT = (By.XPATH, ".//input[contains(@placeholder,'Когда')]")
    RENTAL_PERIOD_INPUT = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    RENTAL_PERIOD_LIST = (By.XPATH, ".//div[@class='Dropdown-menu']")
    COLOR_INPUT = (By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input")
    COMMENT_INPUT = (By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]")
    MIDDLE_ORDER_BUTTON = (By.XPATH, ".//div[starts-with(@class, 'Order')]/button[text()='Заказать']")
    ACCEPT_ORDER_BUTTON = [By.XPATH, ".//button[text()='Да']"]
    ORDER_NUMBER = [By.XPATH, ".//div[contains(text(),'Номер заказа')]"]
    ORDER_STATUS = [By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]"]
    VIEW_STATUS_BUTTON = [By.XPATH, ".//button[text()='Посмотреть статус']"]

    @staticmethod
    def METRO_LIST_BUTTON(metro_station):
        return [By.XPATH, f".//div[text()='{metro_station}']/parent::button"]