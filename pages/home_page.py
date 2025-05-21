
from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

        self.__homepage_logo = self.page.locator('img[alt="Website for automation practice"]')
        self.__signup_login_button = self.page.locator('a[href="/login"]')
        self.__slider = self.page.locator('section[id="slider"]')
        self.__main_section = self.page.locator('//section[2]')
        self.__delete_account_btn = self.page.locator('a[href="/delete_account"]')
        self.__logged_in_msg = self.page.locator('a:has(i.fa-user)')
        self.__logout_btn = self.page.locator('a[href="/logout"]')


    def check_homepage_visibility(self) -> None:
        self.__homepage_logo.wait_for(state='visible')
        assert self.__homepage_logo.is_visible()

        self.__signup_login_button.wait_for(state='visible')
        assert self.__signup_login_button.is_visible()

        self.__slider.wait_for(state='visible')
        assert self.__slider.is_visible()

        self.__main_section.wait_for(state='visible')
        assert self.__main_section.is_visible()

    def click_signup_login_button(self) -> None:
        self.__signup_login_button.click()

    def check_logged_in(self) -> None:
        assert self.__logged_in_msg.is_visible()
    def click_delete_account_btn(self) -> None:
        self.__delete_account_btn.click()

    def logout(self) -> None:
        self.__logout_btn.click()





    def open(self):
        self.page.goto('https://automationexercise.com/')