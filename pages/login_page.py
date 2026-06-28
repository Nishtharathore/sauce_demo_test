import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    URL = "https://www.saucedemo.com/"

    def load(self):
        """Navigate to the login page."""
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """Convenience method: full login flow in one call."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        time.sleep(10)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)