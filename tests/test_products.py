# tests/test_products_sort.py
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class TestProductsSort:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver)
        self.products_page = ProductsPage(driver)

        self.login_page.load()
        self.login_page.login("standard_user", "secret_sauce")

    def test_sort_price_low_to_high(self):
        self.products_page.sort_by("Price (low to high)")
        prices = self.products_page.get_all_prices()
        assert prices == sorted(prices)

    def test_sort_price_high_to_low(self):
        self.products_page.sort_by("Price (high to low)")
        prices = self.products_page.get_all_prices()
        assert prices == sorted(prices, reverse=True)

    def test_sort_name_a_to_z(self):
        self.products_page.sort_by("Name (A to Z)")
        names = self.products_page.get_all_names()
        assert names == sorted(names)

    def test_sort_name_z_to_a(self):
        self.products_page.sort_by("Name (Z to A)")
        names = self.products_page.get_all_names()
        assert names == sorted(names, reverse=True)