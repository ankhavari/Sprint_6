import allure
from utils.constants import Urls
from pages.home_page import HomePage

class TestHomePage:
    @allure.title('Переход к форме создания заказа по кнопке "Заказать" в хэдере')
    @allure.description('Нажимаем кнопку "Заказать" в хэдере страницы, сравниваем текущий url с url страницы заказа')
    def test_tap_header_order_button_open_order_page(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site()
        home_page.click_cookie_confirm()
        home_page.click_header_order_button()
        assert home_page.current_url() == Urls.ORDER_PAGE

    @allure.title('Переход к форме создания заказа по кнопке "Заказать" в теле страницы')
    @allure.description('Нажимаем кнопку "Заказать" в теле страницы после блока "Как это работает", \
    сравниваем текущий url с url страницы заказа')
    def test_tap_finish_order_button_open_order_page(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site()
        home_page.click_cookie_confirm()
        home_page.click_finish_order_button()
        assert home_page.current_url() == Urls.ORDER_PAGE

    @allure.title('Переход на страницу Дзен по нажатию на лого Яндекс')
    @allure.description('Нажимаем на лого Яндекса в хэдере страницы, переключаемся на открывшуюся вкладку, \
    сравниваем текущий url с одним из возможных открывшихся: Dzen, либо капча yandex')
    def test_tap_yandex_logo_open_yandex_page(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site()
        home_page.click_cookie_confirm()
        home_page.click_yandex_logo()
        home_page.switch_window(1)
        home_page.wait_url_until_not_about_blank()
        current_url = home_page.current_url()
        assert (Urls.YANDEX_CAPTCHA_PAGE in current_url) or (Urls.DZEN_MAIN_PAGE in current_url)
