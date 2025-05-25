from playwright.sync_api import Page

from conftest import capture_screenshot

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

        self.__product_list = self.page.locator('div.features-items')
        self.__first_product_view_btn = self.page.locator('a[href="/product_details/1"]')
        self.__product_name = self.page.locator('div.product-information > h2')
        self.__product_category = self.page.locator('div.product-information > p').first
        self.__product_price = self.page.locator('div.product-information > span > span')
        self.__product_availability = self.page.locator('div.product-information > p:nth-child(6)')
        self.__product_condition = self.page.locator('div.product-information > p:nth-child(7)')
        self.__product_brand = self.page.locator('div.product-information > p:nth-child(8)')
        self.__search_product_input = self.page.locator('#search_product')
        self.__search_product_button = self.page.locator('#submit_search')
        self.__searched_product_name = self.page.locator('div.single-products > div.productinfo.text-center > p')

    def click_first_product_view_btn(self):
        self.__first_product_view_btn.click()

    def verify_product_details(self):
        self.__product_name.is_visible()
        self.__product_category.is_visible()
        self.__product_price.is_visible()
        self.__product_availability.is_visible()
        self.__product_condition.is_visible()
        self.__product_brand.is_visible()
        capture_screenshot(self.page, 'product_details')

    def search_product_by_name(self):
        product_search_name = 'Blue Top'
        self.__search_product_input.fill(product_search_name)
        self.__search_product_button.click()
        self.__searched_product_name.wait_for(state='visible')
        assert self.__searched_product_name.text_content() == 'Blue Top'
        capture_screenshot(self.page, 'search_product_success')


