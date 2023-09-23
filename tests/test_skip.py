"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from qa_guru_7_16_pytest_params.application import app
from selene import browser
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


def test_github_desktop(setup_browser):
    if browser.config.window_width < 1012:
        pytest.skip(reason="Not desktop resolution")
    app.open()
    app.header.click_on_sign_in_button()
    app.login_page.should_be_opened()


def test_github_mobile(setup_browser):
    if browser.config.window_width > 1011:
        pytest.skip(reason="Not mobile resolution")
    app.open()
    app.header.open_burger_menu()
    app.header.click_on_sign_in_button()
    app.login_page.should_be_opened()
