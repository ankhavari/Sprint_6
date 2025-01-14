import allure
import pytest

from utils.constants import Urls
from utils.locators import OrderPageLocator
from utils.test_data import TestData as test_data
from pages.order_page import OrderPage
from pages.home_page import HomePage

class TestOrder:
    @allure.title('При создании заказа с корректными данными появляется всплывающее окно с сообщением об успешном оформлении заказа')
    @allure.description('Переходим к созданию заказа, вводим корректные тестовые данные, \
    ищем элемент с нотификацией об успешном оформлении заказа и проверяем, что его текст == "Заказ оформлен"')

    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_placing_order_by_using_top_order_button_positive_result(self, driver, data_set):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        home_page = HomePage(driver)
        home_page.click_cookie_confirm()
        order_page.fill_first_form(test_data.data_sets[data_set])
        order_page.tap_next()
        order_page.fill_second_form(test_data.data_sets[data_set])
        order_page.tap_order()
        order_page.accept_order()
        status = driver.find_element(*OrderPageLocator.ORDER_STATUS)

        assert 'Заказ оформлен' in status.text

    @allure.title('Переход на главную страницу Самоката при нажатии на лого Самоката')
    @allure.description('Переходим на страницу оформления заказа, нажимаем на лого Самоката, \
    получаем текущий url и сравниваем его с url главной страницы самоката')
    def test_tap_samokat_logo_open_main_page(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        order_page.click_samokat_logo()
        current_url = driver.current_url
        assert Urls.MAIN_PAGE in current_url
