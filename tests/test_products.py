import pytest

from pages.home_page import HomePage
from pages.products_page import ProductsPage


class TestProducts:

    @pytest.fixture(autouse=True)
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})

        self.homepage = HomePage(self.page)
        self.productspage = ProductsPage(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_products_and_products_detail_page(self):
        self.homepage.check_homepage_visibility()
        self.homepage.click_products_btn()
        assert self.page.url == 'https://automationexercise.com/products'
        self.productspage.click_first_product_view_btn()
        self.productspage.verify_product_details()

    def test_search_products(self):
        self.homepage.check_homepage_visibility()
        self.homepage.click_products_btn()
        assert self.page.url == 'https://automationexercise.com/products'

        self.productspage.search_product_by_name()



