import pytest

from pages.home_page import HomePage
from pages.sign_page import SignPage
from pages.account_created_page import CreatedPage
from pages.deleteAccount_page import DeletePage
from utils.actions import UserActions


class TestRegisterAndLogin:

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

        user_actions.register_user()

        self.homepage.check_logged_in()
        self.homepage.click_delete_account_btn()
        self.deletedpage.check_account_deleted_and_continue()


    def test_login_correct(self, test_setup):
        """Test to verify login with correct credentials"""

        user_actions = UserActions(
            homepage=self.homepage,
            signpage=self.signpage,
            createdpage=self.createdpage
        )

        user_actions.register_user()
        self.homepage.logout()
        self.homepage.open()
        self.homepage.click_signup_login_button()
        self.signpage.check_login_label_visibility()
        self.signpage.login_correct()
        self.homepage.check_logged_in()
        self.homepage.logout()


    def test_login_incorrect(self, test_setup):
        """Test to verify login with incorrect credentials"""

        self.homepage.click_signup_login_button()
        self.signpage.check_login_label_visibility()
        self.signpage.login_incorrect()
        self.signpage.check_incorrect_login_label_visibility()


    def test_logout(self, test_setup):
        """Test to verify logout functionality"""

        self.homepage.click_signup_login_button()
        self.signpage.check_login_label_visibility()
        self.signpage.login_correct()
        self.homepage.check_logged_in()
        self.homepage.logout()
        assert self.page.url == 'https://automationexercise.com/login'


    def test_register_existing_email(self, test_setup):
        """Test to check response to registering with  existing email"""

        self.homepage.click_signup_login_button()
        self.signpage.check_new_user_label_visibility()
        self.signpage.fill_signup_with_existing_email()
        self.signpage.check_signup_error_message()
