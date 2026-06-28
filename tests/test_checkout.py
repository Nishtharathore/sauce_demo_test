import pytest
import pages



class TestCheckout:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = pages.LoginPage(driver)
        self.products_page = pages.ProductsPage(driver)
        self.cart_page = pages.CartPage(driver)
        self.checkout_page = pages.CheckoutPage(driver)

        # Every checkout test needs to start logged in
        self.login_page.load()
        self.login_page.login("standard_user", "secret_sauce")

    def test_successful_checkout(self):
        self.products_page.add_item_to_cart_by_name("Sauce Labs Backpack")
        self.products_page.click_cart_icon()

        self.cart_page.click_checkout()
        self.checkout_page.enter_checkout_info("John", "Doe", "12345")
        self.checkout_page.click_continue()
        self.checkout_page.click_finish()

        assert self.checkout_page.get_complete_header_text() == "Thank you for your order!"

    def test_checkout_missing_first_name(self):
        self.products_page.add_item_to_cart_by_name("Sauce Labs Backpack")
        self.products_page.click_cart_icon()

        self.cart_page.click_checkout()
        self.checkout_page.enter_checkout_info("", "Doe", "12345")
        self.checkout_page.click_continue()

        assert "First Name is required" in self.checkout_page.get_error_message()

    def test_cart_shows_correct_item_count(self):
        self.products_page.add_item_to_cart_by_name("Sauce Labs Backpack")
        self.products_page.add_item_to_cart_by_name("Sauce Labs Bike Light")
        self.products_page.click_cart_icon()

        assert self.cart_page.get_item_count() == 2

    def test_remove_item_from_cart(self):
        self.products_page.add_item_to_cart_by_name("Sauce Labs Backpack")
        self.products_page.add_item_to_cart_by_name("Sauce Labs Bike Light")
        self.products_page.click_cart_icon()

        self.cart_page.remove_item_by_name("Sauce Labs Backpack")

        assert self.cart_page.get_item_count() == 1
        assert "Sauce Labs Backpack" not in self.cart_page.get_item_names()