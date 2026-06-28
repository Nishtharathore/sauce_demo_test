# pages/products_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage


class ProductsPage(BasePage):
    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def sort_by(self, option_text):
        """option_text examples: 'Price (low to high)', 'Name (A to Z)'"""
        dropdown_element = self.find(self.SORT_DROPDOWN)
        select = Select(dropdown_element)
        select.select_by_visible_text(option_text)

    def get_all_prices(self):
        price_elements = self.driver.find_elements(*self.ITEM_PRICES)
        return [float(el.text.replace("$", "")) for el in price_elements]

    def get_all_names(self):
        name_elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [el.text for el in name_elements]

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def add_item_to_cart_by_name(self, item_name):
        """Find the 'Add to cart' button for a specific product by its display name."""
        button_locator = (
            By.XPATH,
            f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        )
        self.click(button_locator)

    def get_cart_count(self):
        """Return number of items in cart. Returns 0 if badge isn't showing (empty cart)."""
        if self.is_visible(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def click_cart_icon(self):
        self.click(self.CART_LINK)

    def get_all_item_names(self):
        """Return a list of all product names currently visible on the page."""
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        names = []
        for item in items:
            name_element = item.find_element(By.CLASS_NAME, "inventory_item_name")
            names.append(name_element.text)
        return names