import allure

import urls
from pages.lk_page import LkPage


class TestLk:
    @allure.title('Проверка перехода в историю заказов')
    @allure.description('Создается пользователь, происходит переход в историю заказов')
    def test_go_to_history(self, login):
        driver = login[0]
        lk_page = LkPage(driver)
        lk_page.go_to_history()

        assert lk_page.get_current_url() == urls.URL_HISTORY

    @allure.title('Проверка выхода из профиля')
    @allure.description('Создается пользователь, пользователь выходит из профиля')
    def test_logout(self, login):
        driver = login[0]
        lk_page = LkPage(driver)
        lk_page.logout()

        assert lk_page.get_current_url() == urls.URL_LOGIN
