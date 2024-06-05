import pytest
from selenium import webdriver
import urls
from helpers.api_helper import ApiHelper
from pages.login_page import LoginPage


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.fullscreen_window()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()


    browser.get(urls.URL_BASE)

    yield browser

    browser.quit()

@pytest.fixture()
def user():
    user_data = ApiHelper.create_user()

    yield user_data

    ApiHelper.delete_user(user_data)


@pytest.fixture()
def login(driver, user):
    login_page = LoginPage(driver)
    login_page.login(user["email"], user["password"])

    return driver, user

