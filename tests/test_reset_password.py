import allure

import urls
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage


class TestResetPassword:
    @allure.title('Проверка нажатия на кнопку восстановления пароля')
    @allure.description('Происходит нажатие на кнопку восстановления пароля и проверяется переход на страницу ввода email')
    def test_click_reset_button(self,driver):
        login_page = LoginPage(driver)
        login_page.click_reset_password()

        assert login_page.get_current_url() == urls.URL_FORGOT_PASSWORD

    @allure.title('Проверка ввода email на странице забытого пароля')
    @allure.description('Происходит заполнение поля email, нажимается кнопка восстановления пароля, проверяется переход на страницу ввода нового пароля')
    def test_input_email(self, driver):
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.reset_password()

        assert forgot_password.get_current_url() == urls.URL_RESET_PASSWORD

    @allure.title('Проверка что при нажатии на кнопку показать пароль, поле становится активным')
    @allure.description('Происходит нажатие на кнопку показать пароль и проверяется, что поле стало активным')
    def test_show_password(self, driver):
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.reset_password()
        forgot_password.click_eye_button()

        assert forgot_password.password_field_is_active() == 'true'
