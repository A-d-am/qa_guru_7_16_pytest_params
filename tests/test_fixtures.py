"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser
from qa_guru_7_16_pytest_params.application import app


@pytest.fixture()
def open_desktop_browser(open_browser):
    browser.config.window_height = 1080
    browser.config.window_width = 1920


@pytest.fixture()
def open_mobile_browser(open_browser):  # iPhone 12 Pro
    browser.config.window_height = 844
    browser.config.window_width = 390


def test_github_desktop(open_desktop_browser):
    app.open()
    app.header.click_on_sign_in_button()
    app.login_page.should_be_opened()


def test_github_mobile(open_mobile_browser):
    app.open()
    app.header.open_burger_menu()
    app.header.click_on_sign_in_button()
    app.login_page.should_be_opened()
