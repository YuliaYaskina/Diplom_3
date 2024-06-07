import allure

import urls
from pages.main_page import MainPage


class TestMain:
    @allure.title('Проверка перехода в личный кабинет залогиненым пользователем')
    @allure.description('Создается пользователь, происходит переход в личный кабинет, проверяется наличие кнопки "Сохранить"')
    def test_lk_button_with_auth(self, login):
        driver = login[0]
        main_page = MainPage(driver)
        main_page.click_lk_button()

        assert main_page.save_button_is_present() == 'true'

    @allure.title('Проверка перехода в личный кабинет незалогиненным пользователем')
    @allure.description('Происходит переход в личный кабинет, проверяется наличие кнопки "Войти"')
    def test_lk_button_no_auth(self, driver):
        main_page = MainPage(driver)
        main_page.click_lk_button()

        assert main_page.enter_button_is_present() == 'true'

    @allure.title('Проверка перехода в ленту заказов')
    @allure.description('Происходит переход в ленту заказов, проверяется текущий URL')
    def test_order_list_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_list_button()

        assert main_page.get_current_url() == urls.URL_ORDER_LIST

    @allure.title('Проверка перехода в конструктор')
    @allure.description('Происходит переход в личный кабинет, нажимается кнопка перехода в конструктор, проверяется текущий URL')
    def test_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_lk_button()
        main_page.click_constructor_button()

        assert main_page.get_current_url() == urls.URL_BASE

    @allure.title('Проверка открытия окошка с информацией об ингредиентах')
    @allure.description('Происходит нажатие на первый ингредиент, проверяется, что открывается поп-ап с информацией')
    def test_pop_up_ingredients(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient_button()

        assert main_page.pop_up_with_ingredient_is_present() == 'true'

    @allure.title('Проверка закрытия окошка с информацией об ингредиенте')
    @allure.description('Происходит нажатие на первый ингредиент, после открытия поп-апа нажимается крестик, проверяется, что поп-ап закрыт')
    def test_close_pop_up_with_ingredients(self, driver):
        main_page = MainPage(driver)
        main_page.close_pop_up_with_ingredient()

        assert main_page.pop_up_with_ingredient_is_closed() == 'true'

    @allure.title('Проверка добавления ингредиента')
    @allure.description('Первый ингредиент перетаскиваетс в конструктор, проверяется, счетчик количества выбранного ингредиента')
    def test_drag_and_drop_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient(driver)

        assert main_page.get_text_from_ingredient_counter() == "2"

    @allure.title('Проверка создания заказа')
    @allure.description('Создается пользователь, создается заказ, происходит проверка наличия номера заказа')
    def test_create_order(self, login):
        driver = login[0]
        main_page = MainPage(driver)
        main_page.create_order()
        main_page.wait_for_loader_to_be_visible()
        main_page.wait_for_loader_to_be_invisible()

        assert main_page.order_number_is_present() == 'true'