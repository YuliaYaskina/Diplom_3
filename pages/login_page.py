from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators_main
from locators.login_locators import LoginLocators as Locators_login

class LoginPage(BasePage):
    def click_reset_password(self):
        lk_button = self.wait_element_to_be_clickable(Locators_main.lk_button)
        self.driver.execute_script("arguments[0].click();", lk_button)
        reset_password = self.wait_element_to_be_clickable(Locators_login.reset_password)
        self.driver.execute_script("arguments[0].click();", reset_password)

    def login(self, login, password):
        lk_button = self.wait_element_to_be_clickable(Locators_main.lk_button)
        self.driver.execute_script("arguments[0].click();", lk_button)
        self.wait_element_to_be_clickable(Locators_login.email_field_login).send_keys(login)
        self.wait_element_to_be_clickable(Locators_login.password_field_login).send_keys(password)
        enter_button_login = self.wait_element_to_be_clickable(Locators_login.enter_button_login)
        self.driver.execute_script("arguments[0].click();", enter_button_login)
        self.wait_element_to_be_clickable(Locators_main.make_order_button)
