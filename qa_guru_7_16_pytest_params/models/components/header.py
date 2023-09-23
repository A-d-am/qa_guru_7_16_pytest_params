from selene import browser


# noinspection PyMethodMayBeStatic
class Header:

    def click_on_sign_in_button(self):
        browser.element('[href="/login"]').click()

    def open_burger_menu(self):
        browser.element('.Button--link.Button--medium').click()
