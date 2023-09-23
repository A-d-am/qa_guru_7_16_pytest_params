from qa_guru_7_16_pytest_params.models.components.header import Header
from qa_guru_7_16_pytest_params.models.pages.login_page import LoginPage
from selene import browser


# noinspection PyMethodMayBeStatic
class Application:

    def __init__(self):
        self.header = Header()
        self.login_page = LoginPage()

    def open(self):
        browser.open('/')


app = Application()
