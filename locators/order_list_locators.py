from selenium.webdriver.common.by import By

class OrderListLocators:
    last_order_number_locator = [By.XPATH, ".//p[@class = 'text text_type_digits-default']"]
    pop_up_details = [By.XPATH, ".//section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"]
    order_in_work_number = (By.XPATH, "(//li[contains(@class, 'text text_type_digits-default mb-2')])[6][1]")