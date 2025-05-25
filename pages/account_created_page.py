from playwright.sync_api import Page

from conftest import capture_screenshot

class CreatedPage:
    def __init__(self, page: Page):
        self.page = page

        self.__label_account_created = self.page.locator('h2[data-qa="account-created"]')
        self.__continue_btn = self.page.locator('a[data-qa="continue-button"]')

    def check_account_created_and_continue(self):
        assert self.__label_account_created.is_visible()
        capture_screenshot(self.page, 'account_created')
        self.__continue_btn.click()