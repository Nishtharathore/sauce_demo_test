# pages/cart_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTON = (By.XPATH, ".//button[contains(@id, 'remove')]")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def get_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_item_names(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return [item.find_element(*self.ITEM_NAME).text for item in items]

    def remove_item_by_name(self, item_name):
        item_locator = (
            By.XPATH,
            f"//div[text()='{item_name}']/ancestor::div[@class='cart_item']"
        )
        item = self.driver.find_element(*item_locator)
        remove_button = item.find_element(*self.REMOVE_BUTTON)
        remove_button.click()

    def click_checkout(self):
        self.is_visible(self.CHECKOUT_BUTTON)
        self.click(self.CHECKOUT_BUTTON)

    def click_continue_shopping(self):
        self.is_visible(self.CONTINUE_SHOPPING_BUTTON)
        self.click(self.CONTINUE_SHOPPING_BUTTON)