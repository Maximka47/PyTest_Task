from pages.home_page import HomePage
from pages.sign_page import SignPage
from pages.account_created_page import CreatedPage

class UserActions:
    def __init__(self, homepage, signpage, createdpage):
        self.homepage = homepage
        self.signpage = signpage
        self.createdpage = createdpage

    def register_user(self):
        self.homepage.check_homepage_visibility()
        self.homepage.click_signup_login_button()

        self.signpage.check_new_user_label_visibility()
        self.signpage.fill_new_user_signup()

        self.signpage.check_enter_new_message_visibility()
        self.signpage.fill_signup_form()
        self.signpage.click_register_button()

        self.createdpage.check_account_created_and_continue()
