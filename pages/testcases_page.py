from playwright.sync_api import Page

from conftest import capture_screenshot


class AutomationTestCasesPage:
    def __init__(self, page: Page):
        self.page = page

        self.__page_title = self.page.locator('h2.title')
        self.__tests = self.page.locator('div.panel-heading')

    def verify_test_cases_page(self) -> None:
        assert self.__page_title.is_visible()

        for element in self.__tests.all():
            assert element.is_visible()

        capture_screenshot(self.page, 'verify_test_cases_page')

        assert self.__tests.count() == 27


