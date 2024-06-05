import allure

from pages.lk_page import LkPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.order_list_page import OrderListPage

class TestOrderList:
    @allure.title('Проверка открытия окошка с деталями заказа')
    @allure.description('Создается пользователь, создается заказ, происходит проверка открытия поп-апа с деталями заказа')
    def test_order_details(self, login):
        driver = login[0]
        order_list = OrderListPage(driver)
        order_list.click_last_order(driver)

        assert order_list.order_details_pop_up_is_present() == 'true'

    @allure.title('Проверка наличия заказа из истории заказов в ленте заказов')
    @allure.description('Создается пользователь, создается заказ, происходит проверка, что новый заказ присутствует в ленте заказов')
    def test_orders_list_and_history(self, login):
        driver = login[0]
        main_page = MainPage(driver)
        main_page.create_order()
        main_page.click_order_list_button()
        lk_page = LkPage(driver)
        lk_page.go_to_history()
        order_list = OrderListPage(driver)
        order_number_from_list = order_list.get_last_number_order_from_list()
        order_history = OrderHistoryPage(driver)
        order_number_from_history = order_history.get_last_order_number_from_history()
        assert order_number_from_history == order_number_from_list

    @allure.title('Проверка что новый заказ попадает в раздел "В работе"')
    @allure.description('Создается пользователь, создается заказ, происходит проверка что новый заказ попадает в раздел "В работе"')
    def test_order_number(self, login):
        driver = login[0]
        main_page = MainPage(driver)
        main_page.create_order()
        main_page.wait_for_loader_to_be_visible()
        main_page.wait_for_loader_to_be_invisible()
        main_page.click_order_list_button()
        assert main_page.get_order_in_work_number() == f'0{main_page.get_order_number()}'

    @allure.title('Проверка что при создании нового заказа увеличивается счетчик общего числа заказов')
    @allure.description('Создается пользователь, создается заказ, происходит проверка что общее число заказов равно текущему номеру заказа')
    def test_total_number_of_orders(self, login):
        driver = login[0]
        main_page = MainPage(driver)
        main_page.create_order()
        main_page.wait_for_loader_to_be_visible()
        main_page.wait_for_loader_to_be_invisible()
        main_page.click_order_list_button()
        assert main_page.get_total_number_of_orders() == main_page.get_order_number()

    @allure.title('Проверка что при создании нового заказа увеличивается счетчик заказов за сегодня')
    @allure.description('Создается пользователь, создается заказ, происходит проверка число заказов за сегодня увеличилось на 1')
    def test_today_number_of_orders(self,login):
        driver = login[0]
        main_page = MainPage(driver)
        main_page.click_order_list_button()
        today_number_of_orders_before_order = int(main_page.get_today_number_of_orders())
        main_page.go_to_constructor()
        main_page.create_order()
        main_page.wait_for_loader_to_be_visible()
        main_page.wait_for_loader_to_be_invisible()
        main_page.click_order_list_button()
        assert main_page.get_today_number_of_orders() == str(today_number_of_orders_before_order + 1)


