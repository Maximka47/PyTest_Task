import pytest

from pages.home_page import HomePage
from pages.sign_page import SignPage
from pages.account_created_page import CreatedPage
from pages.deleteAccount_page import DeletePage
from utils.actions import UserActions


class TestRegister:

    @pytest.fixture(autouse=True)
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.homepage = HomePage(self.page)
        self.signpage = SignPage(self.page)
        self.createdpage = CreatedPage(self.page)
        self.deletedpage = DeletePage(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_register_functionality(self, test_setup):
        """Test to verify the functionality of registration"""
        
        user_actions = UserActions(
            homepage=self.homepage,
            signpage=self.signpage,
            createdpage=self.createdpage
        )
        self.homepage.check_homepage_visibility()
        self.homepage.click_signup_login_button()

        self.signpage.check_new_user_label_visibility()
        self.signpage.fill_new_user_signup()

        self.signpage.check_enter_new_message_visibility()
        self.signpage.fill_signup_form()
        self.signpage.click_register_button()

        self.createdpage.check_account_created_and_continue()
        self.homepage.check_logged_in()
        self.homepage.click_delete_account_btn()
        self.deletedpage.check_account_deleted_and_continue()

