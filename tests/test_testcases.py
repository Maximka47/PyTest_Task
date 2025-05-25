import pytest

from pages.home_page import HomePage
from pages.testcases_page import AutomationTestCasesPage


class TestContactUs:

    @pytest.fixture(autouse=True)
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})

        self.homepage = HomePage(self.page)
        self.testpage = AutomationTestCasesPage(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_contact_page(self, page):
        self.homepage.check_homepage_visibility()
        self.homepage.click_test_cases_btn()
        assert page.url == "https://automationexercise.com/test_cases"
        self.testpage.verify_test_cases_page()