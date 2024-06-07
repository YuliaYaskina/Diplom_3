import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    @allure.step('Создание экземпляра страницы')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем элемент после ожидания')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ждем, когда элемент станет кликабельным')
    def wait_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Получаем текст элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Проеряем наличие элемента')
    def element_is_present(self, locator):
        try:
            self.find_element_with_wait(locator),
            result = "true"
        except AssertionError:
            result = "false"

        return result

    @allure.step('Перемещение по заданному url')
    def navigation(self, url):
        self.driver.get(url)

    @allure.step('Ожидаем, когда элемент станет видимым')
    def wait_for_element_to_be_visible(self, locator):
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидаем, когда элемент станет невидимым')
    def wait_for_element_to_be_invisible(self, locator):
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Кликаем на элемент')
    def click_the_element(self, element_to_click):
        self.driver.execute_script("arguments[0].click();", element_to_click)
