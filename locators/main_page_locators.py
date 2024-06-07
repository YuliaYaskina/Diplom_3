from selenium.webdriver.common.by import By


class MainPageLocators:
    lk_button = [By.XPATH, ".//p[text()='Личный Кабинет']"]
    collect_burger_title = [By.XPATH, ".//р1[text()='Соберите бургер']"]
    make_order_button = [By.XPATH, ".//button[text()='Оформить заказ']"]
    order_list = [By.XPATH, ".//p[text()='Лента Заказов']"]
    constructor = [By.XPATH, ".//p[text()='Конструктор']"]
    enter_account = [By.XPATH, ".//button[text()='Войти в аккаунт']"]
    ingredient_details = [By.XPATH, ".//section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"]
    ingredient_details_closed = [By.XPATH, ".//section[@class = 'Modal_modal__P3_V5']"]
    first_igredient = [By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']"]
    close_ingredient_pop_up = [By.XPATH, ".//button[@type='button']"]
    ingredient_constructor = [By.XPATH, ".//span[text()='Перетяните булочку сюда (верх)']"]
    ingredient_counter = [By.XPATH, ".//p[@class ='counter_counter__num__3nue1']"]
    create_order = [By.XPATH, ".//button[text()='Оформить заказ']"]
    close_order_window = [By.XPATH, ".//button[@class ='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
    new_order_number = [By.XPATH, ".//h2[@class = 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']" ]
    loader = [By.XPATH, ".//img[@class = 'Modal_modal__loading__3534A']"]
    total_number_of_orders = [By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ')])[1]"]
    today_number_of_orders = [By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ')])[2]"]
