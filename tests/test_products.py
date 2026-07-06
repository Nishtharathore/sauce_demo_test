import pytest
import pages


class TestProductsSort:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = pages.LoginPage(driver)
        self.products_page = pages.ProductsPage(driver)
        self.login_page.load()
        self.login_page.login("standard_user", "secret_sauce")

    @pytest.mark.tags("smoke", "regression")
    @pytest.mark.parametrize("sort_option, key, reverse", [
        ("Price (low to high)", "price", False),
        ("Price (high to low)", "price", True),
        ("Name (A to Z)", "name", False),
        ("Name (Z to A)", "name", True),
    ])
    def test_sort(self, sort_option, key, reverse):
        self.products_page.sort_by(sort_option)
        if key == "price":
            items = self.products_page.get_all_prices()
        else:
            items = self.products_page.get_all_names()
        assert items == sorted(items, reverse=reverse)