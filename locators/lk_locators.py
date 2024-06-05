from selenium.webdriver.common.by import By


class LkLocators:
    save_button = [By.XPATH, ".//button[text()='Сохранить']"]
    history = [By.XPATH, ".//a[text() = 'История заказов']"]
    logout = [By.XPATH, ".//button[text() = 'Выход']"]
    active_history = [By.XPATH, ".//[@class = 'История заказов']"]