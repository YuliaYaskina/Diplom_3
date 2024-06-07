from selenium.webdriver.common.by import By


class LoginLocators:
    reset_password = [By.XPATH, ".//a[text()='Восстановить пароль']"]
    email_field_login = [By.XPATH, ".//input[@name = 'name']"]
    password_field_login = [By.XPATH, ".//input[@name = 'Пароль']"]
    enter_button_login = [By.XPATH, ".//button[text() = 'Войти']"]

