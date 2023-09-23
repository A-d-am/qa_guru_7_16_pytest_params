from selene import browser, have, be


class LoginPage:
    login_url = 'https://github.com/login'

    def should_be_opened(self):
        current_url = browser.driver.current_url
        assert current_url == self.login_url, f'Expected {self.login_url} is opened, got {current_url}'
