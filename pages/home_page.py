from conftest import capture_screenshot
from data.user_data import valid_user
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
        self.__contact_us_btn = self.page.locator('a[href="/contact_us"]')
        self.__test_cases_btn = self.page.locator('a:has(i.fa-list)').first
        self.__products_btn = self.page.locator('a:has(i.card_travel)')
        self.__subscription_title = self.page.locator('div.single-widget > h2')
        self.__subscription_input = self.page.locator('#susbscribe_email')
        self.__subscription_btn = self.page.locator('#subscribe')
        self.__subscribe_success_msg = self.page.locator('#success-subscribe')


    def check_homepage_visibility(self) -> None:
        self.__homepage_logo.wait_for(state='visible')
        assert self.__homepage_logo.is_visible()

        self.__signup_login_button.wait_for(state='visible')
        assert self.__signup_login_button.is_visible()

        self.__slider.wait_for(state='visible')
        assert self.__slider.is_visible()

        self.__main_section.wait_for(state='visible')
        assert self.__main_section.is_visible()

        capture_screenshot(self.page, 'home_page')

    def click_signup_login_button(self) -> None:
        self.__signup_login_button.click()

    def check_logged_in(self) -> None:
        assert self.__logged_in_msg.is_visible()
    def click_delete_account_btn(self) -> None:
        self.__delete_account_btn.click()

    def logout(self) -> None:
        self.__logout_btn.click()

    def click_contact_us_btn(self) -> None:
        self.__contact_us_btn.click()

    def click_test_cases_btn(self) -> None:
        self.__test_cases_btn.click()

    def click_products_btn(self) -> None:
        self.__products_btn.click()

    def verify_subscription_title(self) -> None:
        assert self.__subscription_title.is_visible()
        assert self.__subscription_title.text_content() == 'Subscription'

    def fill_subscription_form(self) -> None:
        self.__subscription_input.fill(valid_user['email'])
        capture_screenshot(self.page, 'subscription_form')
        self.__subscription_btn.click()
        assert self.__subscribe_success_msg.is_visible()
        capture_screenshot(self.page, 'subscription_form_success')







    def open(self):
        self.page.goto('https://automationexercise.com/')