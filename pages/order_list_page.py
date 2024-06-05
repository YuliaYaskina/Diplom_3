from seletools.actions import drag_and_drop
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators_main
from locators.order_list_locators import OrderListLocators as Locators_orders
from locators.order_list_locators import OrderListLocators as Locators_order_list


class OrderListPage(BasePage):

    def drag_and_drop_ingredient(self, driver):
        source_element = self.find_element_with_wait(Locators_main.first_igredient)
        target_element = self.find_element_with_wait(Locators_main.ingredient_constructor)
        drag_and_drop(driver, source_element, target_element)

    def click_last_order(self, driver):
        self.drag_and_drop_ingredient(driver)
        create_order = self.wait_element_to_be_clickable(Locators_main.create_order)
        self.driver.execute_script("arguments[0].click();", create_order)
        order_list = self.wait_element_to_be_clickable(Locators_main.order_list)
        self.driver.execute_script("arguments[0].click();", order_list)
        last_order = self.wait_element_to_be_clickable(Locators_orders.last_order_number_locator)
        self.driver.execute_script("arguments[0].click();", last_order)

    def order_details_pop_up_is_present(self):
        result = self.element_is_present(Locators_order_list.pop_up_details)
        return result

    def get_last_number_order_from_list(self):
        return self.get_text_from_element(Locators_order_list.last_order_number_locator)



