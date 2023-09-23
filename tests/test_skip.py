"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from qa_guru_7_16_pytest_params.application import app

@pytest.fixture()
def setup_browser(open_browser):
    pass


def test_github_desktop(setup_browser):
    app.open()
    app.header.click_on_sign_in_button()
    app.login_page.should_be_opened()


def test_github_mobile(setup_browser):
    app.open()
    app.header.open_burger_menu()
    app.header.click_on_sign_in_button()
    app.login_page.should_be_opened()
