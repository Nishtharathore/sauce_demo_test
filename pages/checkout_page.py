# pages/checkout_page.py
import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Step 1: Checkout info (name, postal code)
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    # Step 2: Checkout overview
    FINISH_BUTTON = (By.ID, "finish")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    SUBTOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    # Step 3: Checkout complete
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    # --- Step 1 methods ---
    def enter_checkout_info(self, first_name, last_name, postal_code):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        time.sleep(2)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        time.sleep(2)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self):
        self.is_visible(self.CONTINUE_BUTTON)
        self.click(self.CONTINUE_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    # --- Step 2 methods ---
    def get_item_count_in_overview(self):
        return len(self.driver.find_elements(*self.CART_ITEM))

    def get_subtotal_text(self):
        return self.get_text(self.SUBTOTAL_LABEL)

    def get_total_text(self):
        return self.get_text(self.TOTAL_LABEL)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    # --- Step 3 methods ---
    def get_complete_header_text(self):
        return self.get_text(self.COMPLETE_HEADER)

    def click_back_home(self):
        self.click(self.BACK_HOME_BUTTON)