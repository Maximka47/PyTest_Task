from playwright.sync_api import Page

from conftest import capture_screenshot
from data.user_data import valid_user
from data.user_data import invalid_user

class SignPage:
    def __init__(self, page: Page):
        self.page = page

        self.__new_user_label = self.page.locator('div[class="signup-form"] > h2')
        self.__new_user_name = self.page.locator('input[data-qa="signup-name"]')
        self.__new_user_email = self.page.locator('input[data-qa="signup-email"]')
        self.__new_user_signup_btn = self.page.locator('button[data-qa="signup-button"]')
        self.__signup_label = self.page.locator('div[class="login-form"] > h2')
        self.__radio_male = self.page.locator('#id_gender1')
        self.__form_name = self.page.locator('input[id="name"]')
        self.__form_email = self.page.locator('input[id="email"]')
        self.__form_password = self.page.locator('input[id="password"]')
        self.__select_days = self.page.locator('select[id="days"]')
        self.__select_months = self.page.locator('select[id="months"]')
        self.__select_years = self.page.locator('select[id="years"]')
        self.__news_box = self.page.locator('input[id="newsletter"]')
        self.__optin_box = self.page.locator('input[id="optin"]')
        self.__country_select = self.page.locator('select[id="country"]')
        self.__form_firstname = self.page.locator('input[id="first_name"]')
        self.__form_lastname = self.page.locator('input[id="last_name"]')
        self.__form_company = self.page.locator('input[id="company"]')
        self.__form_address = self.page.locator('input[id="address1"]')
        self.__form_state = self.page.locator('input[id="state"]')
        self.__form_city = self.page.locator('input[id="city"]')
        self.__form_zip = self.page.locator('input[id="zipcode"]')
        self.__form_mobile = self.page.locator('input[id="mobile_number"]')
        self.__create_btn = self.page.locator('button[data-qa="create-account"]')
        self.__login_email = self.page.locator('input[data-qa="login-email"]')
        self.__login_password = self.page.locator('input[data-qa="login-password"]')
        self.__login_button = self.page.locator('button[data-qa="login-button"]')
        self.__login_label = self.page.locator('div[class="login-form"] > h2')
        self.__incorrect_login_label = self.page.locator('form[action="/login"] > p')
        self.__signup_error_message = self.page.locator('form[action="/signup"] > p')


    def check_new_user_label_visibility(self) -> None:
        assert self.__new_user_label.is_visible()
    def check_enter_new_message_visibility(self) -> None:
        assert self.__signup_label.is_visible()

    def fill_new_user_signup(self) -> None:
        self.__new_user_name.fill(valid_user['name'])
        self.__new_user_email.fill(valid_user['email'])
        capture_screenshot(self.page, 'fill_new_user_signup')
        self.__new_user_signup_btn.click()


    def fill_signup_form(self) -> None:
        self.__radio_male.check()
        self.__form_password.fill(valid_user['password'])
        self.__select_days.select_option(value='1')
        self.__select_months.select_option(value='1')
        self.__select_years.select_option(value='2000')
        self.__news_box.click()
        self.__optin_box.click()
        self.__form_firstname.fill(valid_user['first_name'])
        self.__form_lastname.fill(valid_user['last_name'])
        self.__form_company.fill(valid_user['company'])
        self.__form_address.fill(valid_user['address'])
        self.__country_select.select_option(value='United States')
        self.__form_state.fill(valid_user['state'])
        self.__form_city.fill(valid_user['city'])
        self.__form_zip.fill(valid_user['zip'])
        self.__form_mobile.fill(valid_user['mobile_number'])
        capture_screenshot(self.page, 'fill_signup_form')

    def click_register_button(self) -> None:
        self.__create_btn.click()

    def check_login_label_visibility(self) -> None:
        assert self.__login_label.is_visible()

    def login_correct(self) -> None:
        self.__login_email.fill(valid_user['email'])
        self.__login_password.fill(valid_user['password'])
        capture_screenshot(self.page, 'login_correct')
        self.__login_button.click()

    def login_incorrect(self) -> None:
        self.__login_email.fill(invalid_user['email'])
        self.__login_password.fill(invalid_user['password'])
        capture_screenshot(self.page, 'login_incorrect')
        self.__login_button.click()

    def check_incorrect_login_label_visibility(self) -> None:
        assert self.__incorrect_login_label.is_visible()
        assert "incorrect" in self.__incorrect_login_label.text_content()
        capture_screenshot(self.page, 'check_incorrect_login_label_visibility')

    def check_signup_error_message(self) -> None:
        assert self.__signup_error_message.is_visible()
        assert self.__signup_error_message.text_content() == 'Email Address already exist!'
        capture_screenshot(self.page, 'check_signup_error_message')

    def fill_signup_with_existing_email(self):
        self.__new_user_email.fill(valid_user['email'])
        self.__new_user_name.fill("Josh")
        capture_screenshot(self.page, 'fill_signup_with_existing_email')
        self.__new_user_signup_btn.click()


