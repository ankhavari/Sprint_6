import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.locators import OrderPageLocator

class OrderPage(BasePage):
    @allure.step('Ввод имени')
    def input_name(self, name: str):
        return self.find_element(OrderPageLocator.NAME_INPUT).send_keys(name)

    @allure.step('Ввод фамилии')
    def input_surname(self, surname: str):
        return self.find_element(OrderPageLocator.SURNAME_INPUT).send_keys(surname)

    @allure.step('Ввод адреса')
    def input_address(self, address: str):
        return self.find_element(OrderPageLocator.ADDRESS_INPUT).send_keys(address)

    @allure.step('Выбор станции метро')
    def choose_metro(self, metro_station: str):
        self.find_element(OrderPageLocator.METRO_STATION_INPUT).click()
        return self.find_element(OrderPageLocator.METRO_LIST_BUTTON(metro_station)).click()

    @allure.step('Ввод номера телефона')
    def input_phone_number(self, phone_number: str):
        return self.find_element(OrderPageLocator.PHONE_NUMBER_INPUT).send_keys(phone_number)

    @allure.step('Нажать Далее')
    def tap_next(self):
        return self.find_element(OrderPageLocator.NEXT_BUTTON).click()

    @allure.step('Ввод даты')
    def input_date(self, date: str):
        return self.find_element(OrderPageLocator.DATE_INPUT).send_keys(date)

    @allure.step('Выбор срока аренды')
    def choose_rental_period(self, options= int):
        self.find_element(OrderPageLocator.RENTAL_PERIOD_INPUT).click()
        return self.find_elements(OrderPageLocator.RENTAL_PERIOD_LIST)[options].click()

    @allure.step('Выбор цвета самоката')
    def choose_color(self, options= int):
        return self.find_elements(OrderPageLocator.COLOR_INPUT)[options].click()

    @allure.step('Ввод комментария для курьера')
    def input_comment_for_courier(self, comment_for_courier: str):
        return self.find_element(OrderPageLocator.COMMENT_INPUT).send_keys(comment_for_courier)

    @allure.step('Нажать Заказать')
    def tap_order(self):
        return self.find_element(OrderPageLocator.MIDDLE_ORDER_BUTTON).click()

    @allure.step('Подтвердить заказ')
    def accept_order(self):
        return self.find_element(OrderPageLocator.ACCEPT_ORDER_BUTTON).click()

    @allure.step('Заполнить форму "Для кого самокат')
    def fill_first_form(self, data_set: dict):
        self.input_name(data_set['name'])
        self.input_surname(data_set['surname'])
        self.input_address(data_set['address'])
        self.choose_metro(data_set['metro_station'])
        self.input_phone_number(data_set['phone_number'])

    @allure.step('Заполнить форму "Про аренду"')
    def fill_second_form(self, data_set: dict):
        self.input_date(data_set['date'])
        self.choose_rental_period(data_set['rental_period'])
        for option in data_set['color']:
            self.choose_color(option)
        self.input_comment_for_courier(data_set['comment_for_courier'])