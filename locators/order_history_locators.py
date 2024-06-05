from selenium.webdriver.common.by import By


class OrderHistoryLocators:
    last_order_number = [By.XPATH, ".//p[@class = 'text text_type_digits-default']"]
