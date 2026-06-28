from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find(self, locator):
        """Wait until element is present, then return it."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Wait until element is clickable, then click it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        """Wait until element is visible, clear it, then type text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Wait until element is visible, then return its text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_visible(self, locator):
        """Return True if element becomes visible within timeout, else False."""
        return self.wait.until(EC.visibility_of_element_located(locator))