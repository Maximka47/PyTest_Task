from playwright.sync_api import Page

class CreatedPage:
    def __init__(self, page: Page):
        self.page = page

        self.__label_account_created = self.page.locator('h2[data-qa="account-created"]')
        self.__continue_btn = self.page.locator('a[data-qa="continue-button"]')

    def check_account_created_and_continue(self):
        assert self.__label_account_created.is_visible()
        self.__continue_btn.click()