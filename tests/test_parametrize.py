"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser
from qa_guru_7_16_pytest_params.application import app
from selenium import webdriver


@pytest.fixture(params=[[1920, 1080], [390, 844], [380, 850]])
def setup_browser(request):
    browser.config.base_url = 'https://github.com'
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield
    browser.quit()


@pytest.mark.parametrize("setup_browser", [[1512, 982]], indirect=True)
def test_github_desktop(setup_browser):
    app.open()
    app.header.click_on_sign_in_button()
    app.login_page.should_be_opened()


@pytest.mark.parametrize("setup_browser", [[375, 667]], indirect=True)
def test_github_mobile(setup_browser):
    app.open()
    app.header.open_burger_menu()
    app.header.click_on_sign_in_button()
    app.login_page.should_be_opened()
