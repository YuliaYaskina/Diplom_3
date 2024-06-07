from selenium.webdriver.common.by import By

class ResetPasswordLocators:
    save_button = [By.XPATH, ".//button[text()='Сохранить']"]
    password_field = [By.XPATH, ".//label[text()='Пароль']"]
    input_password = [By.XPATH, ".//input[@name='Введите новый пароль']"]
    eye_button = [By.XPATH, ".//div[@class = 'input__icon input__icon-action']"]
    active_password_field = [By.XPATH, ".//label[@class='input__placeholder text noselect text_type_main-default input__placeholder-focused']"]