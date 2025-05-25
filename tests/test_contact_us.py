import os.path

import pytest

from pages.contact_us_page import ContactPage
from pages.home_page import HomePage


class TestContactUs:

    @pytest.fixture(autouse=True)
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})

        self.contactpage = ContactPage(self.page)
        self.homepage = HomePage(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_contact_page(self, page):

        self.homepage.check_homepage_visibility()
        self.homepage.click_contact_us_btn()
        self.contactpage.check_get_in_touch_title()
        self.contactpage.fill_contact_form()
        self.contactpage.check_contact_form_success()
        self.contactpage.click_forms_home_btn()
        self.homepage.check_homepage_visibility()


