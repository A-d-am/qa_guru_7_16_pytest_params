import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture()
def open_browser():
    browser.config.base_url = 'https://github.com'
    driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    yield
    browser.quit()
