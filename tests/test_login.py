import time
import pytest
import pages


class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.web_driver = driver
        self.login_page = pages.LoginPage(self.web_driver)
        self.products_page = pages.ProductsPage(self.web_driver)

    @pytest.mark.tags("regression", "smoke")
    def test_valid_login(self):
        self.login_page.load()
        self.login_page.login("standard_user", "secret_sauce")
        assert self.products_page.get_page_title() == "Products"

    @pytest.mark.tags("regression", "negative")
    @pytest.mark.parametrize("username, password, expected_error", [
        ("standard_user", "wrong_password", "Username and password do not match"),
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out"),
        ("", "", "Username is required"),
    ])
    def test_invalid_login(self, username, password, expected_error):
        self.login_page.load()
        if username or password:
            self.login_page.login(username, password)
        else:
            self.login_page.click_login()
        assert expected_error in self.login_page.get_error_message()