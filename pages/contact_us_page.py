from playwright.sync_api import Page

from conftest import capture_screenshot
from data.user_data import valid_user
import os.path

class ContactPage:
    def __init__(self, page: Page):
        self.page = page

        self.__get_in_touch_title = self.page.locator('div[class="contact-form"] > h2')
        self.__contact_form_name = self.page.locator('input[data-qa="name"]')
        self.__contact_form_email = self.page.locator('input[data-qa="email"]')
        self.__contact_form_subject = self.page.locator('input[data-qa="subject"]')
        self.__contact_form_message = self.page.locator('textarea[data-qa="message"]')
        self.__contact_form_file = self.page.locator('input[type="file"].form-control')
        self.__contact_form_submit_btn = self.page.locator('input[data-qa="submit-button"]')
        self.__contact_form_success_msg = self.page.locator('div.status.alert.alert-success')
        self.__contact_form_home_btn = self.page.locator('a.btn-success')

        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.__file_upload = os.path.join(current_dir, "../data/upload_file.txt")
        assert os.path.isfile(self.__file_upload), f"File not found: {self.__file_upload}"

    def check_get_in_touch_title(self):
        assert self.__get_in_touch_title.is_visible()

    def fill_contact_form(self):
        self.__contact_form_name.fill(valid_user['name'])
        self.__contact_form_email.fill(valid_user['email'])
        self.__contact_form_subject.fill(valid_user['subject'])
        self.__contact_form_message.fill(valid_user['message'])
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.__contact_form_file.wait_for(state="visible")
        self.__contact_form_file.set_input_files(self.__file_upload)
        capture_screenshot(self.page, 'contact_form_filled')
        self.__contact_form_submit_btn.click()


    def check_contact_form_success(self):
        assert self.__contact_form_success_msg.is_visible()
        capture_screenshot(self.page, 'contact_form_success')

    def click_forms_home_btn(self):
        self.__contact_form_home_btn.click()


