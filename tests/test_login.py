import time
import pytest
import pages


class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.web_driver = driver
        self.login_page = pages.LoginPage(self.web_driver)
        self.products_page = pages.ProductsPage(self.web_driver)

    def test_valid_login(self):
        self.login_page.load()
        self.login_page.login("standard_user", "secret_sauce")
        assert self.products_page.get_page_title() == "Products"
        time.sleep(10)

    def test_invalid_password(self):
        self.login_page.load()
        self.login_page.login("standard_user", "wrong_password")
        assert "Username and password do not match" in self.login_page.get_error_message()
        time.sleep(10)

    def test_locked_out_user(self):
        self.login_page.load()
        self.login_page.login("locked_out_user", "secret_sauce")
        assert "Sorry, this user has been locked out" in self.login_page.get_error_message()
        time.sleep(10)

    def test_empty_credentials(self):
        self.login_page.load()
        self.login_page.click_login()
        assert "Username is required" in self.login_page.get_error_message()
        time.sleep(10)
