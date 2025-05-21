from playwright.sync_api import Page

class DeletePage:
    def __init__(self, page: Page):
        self.page = page

        self.__deleted_msg = self.page.locator('h2[data-qa="account-deleted"]')
        self.__continue_btn = self.page.locator('a[data-qa="continue-button"]')

    def check_account_deleted_and_continue(self):
        assert self.__deleted_msg.is_visible()
        self.__continue_btn.click()