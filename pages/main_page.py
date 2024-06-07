from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators as Locators
from locators.login_locators import LoginLocators as Locators_login
from locators.lk_locators import LkLocators as Locators_lk
from seletools.actions import drag_and_drop
from locators.order_list_locators import OrderListLocators as Locators_order_list


class MainPage(BasePage):

    def create_order(self):
        self.drag_and_drop_ingredient(self.driver)
        create_order = self.wait_element_to_be_clickable(Locators.create_order)
        self.click_the_element(create_order)

    def order_number_is_present(self):
        result = self.element_is_present(Locators.new_order_number)
        return result

    def click_lk_button(self):
        lk_button = self.wait_element_to_be_clickable(Locators.lk_button)
        self.click_the_element(lk_button)

    def save_button_is_present(self):
        result = self.element_is_present(Locators_lk.save_button)
        return result

    def enter_button_is_present(self):
        result = self.element_is_present(Locators_login.enter_button_login)
        return result

    def pop_up_with_ingredient_is_present(self):
        result = self.element_is_present(Locators.ingredient_details)
        return result

    def pop_up_with_ingredient_is_closed(self):
        result = self.element_is_present(Locators.ingredient_details_closed)
        return result

    def click_order_list_button(self):
        order_list_button = self.wait_element_to_be_clickable(Locators.order_list)
        self.click_the_element(order_list_button)

    def click_constructor_button(self):
        order_list_button = self.wait_element_to_be_clickable(Locators.order_list)
        self.click_the_element(order_list_button)
        constructor_button = self.wait_element_to_be_clickable(Locators.constructor)
        self.click_the_element(constructor_button)
        self.wait_element_to_be_clickable(Locators.enter_account)

    def click_ingredient_button(self):
        first_ingr = self.wait_element_to_be_clickable(Locators.first_igredient)
        self.click_the_element(first_ingr)

    def close_pop_up_with_ingredient(self):
        first_ingr = self.find_element_with_wait(Locators.first_igredient)
        self.click_the_element(first_ingr)
        close_button = self.wait_element_to_be_clickable(Locators.close_ingredient_pop_up)
        self.click_the_element(close_button)

    def drag_and_drop_ingredient(self, driver):
        source_element = self.find_element_with_wait(Locators.first_igredient)
        target_element = self.find_element_with_wait(Locators.ingredient_constructor)
        drag_and_drop(driver, source_element, target_element)

    def get_text_from_ingredient_counter(self):
        return self.get_text_from_element(Locators.ingredient_counter)

    def get_order_number(self):
        return self.get_text_from_element(Locators.new_order_number)

    def wait_for_loader_to_be_invisible(self):
        self.wait_for_element_to_be_invisible(Locators.loader)

    def wait_for_loader_to_be_visible(self):
        self.wait_for_element_to_be_visible(Locators.loader)

    def get_order_in_work_number(self):
        return self.get_text_from_element(Locators_order_list.order_in_work_number)

    def get_total_number_of_orders(self):
        return self.get_text_from_element(Locators.total_number_of_orders)

    def get_today_number_of_orders(self):
        return self.get_text_from_element(Locators.today_number_of_orders)

    def go_to_constructor(self):
        constructor = self.wait_element_to_be_clickable(Locators.constructor)
        self.click_the_element(constructor)