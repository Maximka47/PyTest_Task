import pytest

from pages.home_page import HomePage

class TestSubscription:

    @pytest.fixture(autouse=True)
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})

        self.homepage = HomePage(self.page)

        self.page.goto('https://automationexercise.com/')
    def test_verify_subscription_in_homepage(self, page):
        self.homepage.check_homepage_visibility()
        self.homepage.verify_subscription_title()
        self.homepage.fill_subscription_form()