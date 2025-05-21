import pytest

from pages.home_page import HomePage
from pages.sign_page import SignPage
from pages.account_created_page import CreatedPage
from pages.deleteAccount_page import DeletePage

from utils.actions import UserActions


class TestLoginIncorrect:

    @pytest.fixture(autouse=True)
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.homepage = HomePage(self.page)
        self.signpage = SignPage(self.page)
        self.createdpage = CreatedPage(self.page)
        self.deletedpage = DeletePage(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_login_incorrect(self, test_setup):
        """Test to verify login with incorrect credentials"""

        user_actions = UserActions(
            homepage=self.homepage,
            signpage=self.signpage,
            createdpage=self.createdpage
        )

        user_actions.register_user()

        self.homepage.click_signup_login_button()

        self.signpage.check_login_label_visibility()
        self.signpage.login_incorrect()
        self.signpage.check_new_user_label_visibility()

        self.page.goto('https://automationexercise.com/')
        self.homepage.click_delete_account_btn()


