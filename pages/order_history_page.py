from pages.base_page import BasePage
from locators.order_history_locators import OrderHistoryLocators as Locators_history

class OrderHistoryPage(BasePage):
    def get_last_order_number_from_history(self):
        return self.get_text_from_element(Locators_history.last_order_number)
