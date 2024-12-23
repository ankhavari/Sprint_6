import allure
import pytest
from utils.locators import HomePageLocators
from utils.test_data import HomePageFaq
from pages.home_page import HomePage

class TestFaq:
    @allure.title('При нажатии на вопрос в выпадающем меню отображается соответствующий текст ответа')
    @allure.description('По очереди прокликиваем каждый вопрос и сравниваем полученный текст ответа с ожидаемым')

    @pytest.mark.parametrize(
        "question, answer, expected_answer",
        [
            (0, 0, HomePageFaq.answer1),
            (1, 1, HomePageFaq.answer2),
            (2, 2, HomePageFaq.answer3),
            (3, 3, HomePageFaq.answer4),
            (4, 4, HomePageFaq.answer5),
            (5, 5, HomePageFaq.answer6),
            (6, 6, HomePageFaq.answer7),
            (7, 7, HomePageFaq.answer8),
        ]
    )
    def test_faq_click_questions_show_answers(self, driver, question, answer, expected_answer):
        home_page = HomePage(driver)
        home_page.go_to_site()
        home_page.click_cookie_confirm()
        home_page.click_faq_question(question_number=question)
        answer = home_page.find_element(HomePageLocators.FAQ_ANSWER_BUTTON(answer_number=answer))

        assert answer.is_displayed() and answer.text == expected_answer, \
            'Текст ответа не совпадает с ожидаемым результатом'