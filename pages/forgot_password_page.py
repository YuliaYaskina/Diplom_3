from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators_main
from locators.login_locators import LoginLocators as Locators_login
from locators.forgot_password_locators import ForgotPasswordPageLocators as Locators_forgot
from locators.reset_password_locators import ResetPasswordLocators as Locators_reset
from helpers.data_generator import DataGenerate

class ForgotPasswordPage(BasePage):
    def reset_password(self):
        lk_button = self.wait_element_to_be_clickable(Locators_main.lk_button)
        self.click_the_element(lk_button)
        reset_password = self.wait_element_to_be_clickable(Locators_login.reset_password)
        self.click_the_element(reset_password)
        email_field = self.wait_element_to_be_clickable(Locators_forgot.email_field)
        self.click_the_element(email_field)
        self.find_element_with_wait(Locators_forgot.email_field_active).send_keys(DataGenerate.email_generator())
        reset_button = self.wait_element_to_be_clickable(Locators_forgot.reset_button)
        self.click_the_element(reset_button)
        self.wait_element_to_be_clickable(Locators_reset.save_button)

    def click_eye_button(self):
        self.reset_password()
        eye_button = self.wait_element_to_be_clickable(Locators_reset.eye_button)
        self.click_the_element(eye_button)

    def get_class_name_visible_password(self):
        object1 = self.find_element_with_wait(Locators_reset.active_password_field)
        object2 = object1.get_attribute('class')

        return object2

    def password_field_is_active(self):
        result = self.element_is_present(Locators_reset.active_password_field)
        return result

