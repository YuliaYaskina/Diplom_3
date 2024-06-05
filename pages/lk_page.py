import urls
from locators.main_page_locators import MainPageLocators as Locators_main
from locators.login_locators import LoginLocators as Locators_login
from locators.lk_locators import LkLocators as Locators_lk
from pages.base_page import BasePage


class LkPage(BasePage):
    def navigate_to_orders_history(self):
        self.navigation(urls.URL_HISTORY)

    def go_to_history(self):
        lk_button = self.wait_element_to_be_clickable(Locators_main.lk_button)
        self.driver.execute_script("arguments[0].click();", lk_button)
        history = self.wait_element_to_be_clickable(Locators_lk.history)
        self.driver.execute_script("arguments[0].click();", history)
        self.get_current_url()

    def logout(self):
        lk_button = self.wait_element_to_be_clickable(Locators_main.lk_button)
        self.driver.execute_script("arguments[0].click();", lk_button)
        login = self.wait_element_to_be_clickable(Locators_lk.logout)
        self.driver.execute_script("arguments[0].click();", login)
        self.wait_element_to_be_clickable(Locators_login.enter_button_login)
