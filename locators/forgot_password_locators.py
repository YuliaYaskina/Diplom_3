from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    email_field = [By.XPATH, ".//label[text()='Email']"]
    email_field_active = [By.XPATH,".//input"]
    reset_button = [By.XPATH, ".//button[text()='Восстановить']"]