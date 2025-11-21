
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        # Define your element locators as tuples
        self.product_button = (By.XPATH, '//a[@href="/products" and contains(text(), "Products")]')
        self.women_category_button  = (By.XPATH, '//a[@href="#Women"]')
        self.dress_category_button = (By.XPATH, '//a[contains(text(), "Dress")]')
        self.dress_tile = (By.XPATH, "//a[@href='/product_details/3']")  # Changed attribute name for clarity

    def click_product_button(self, retries=3):
        """Clicks the 'Products' button, retrying on StaleElementReferenceException."""
        for attempt in range(retries):
            try:
                # Wait for element to be clickable before clicking
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.product_button)
                ).click()
                return # Success, so exit the function
            except StaleElementReferenceException:
                # If element goes stale, print warning and retry
                print(f"[WARNING] StaleElementReferenceException on product_button click, retrying ({attempt+1}/{retries})")
                # If all retries fail, raise an error
        raise Exception("Failed to click 'Products' button due to repeated StaleElementReferenceException.")

    def click_women_category_button(self, retries=3):
        """Clicks the 'Women' category button."""
        for attempt in range(retries):
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.women_category_button)
                ).click()
                return
            except StaleElementReferenceException:
                print(f"[WARNING] StaleElementReferenceException on women_category_button click, retrying ({attempt+1}/{retries})")
        raise Exception("Failed to click 'Women' category button due to repeated StaleElementReferenceException.")

    def click_dress_category_button(self, retries=3):
        """Clicks the 'Dress' category button."""
        for attempt in range(retries):
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.dress_category_button)
                ).click()
                return
            except StaleElementReferenceException:
                print(f"[WARNING] StaleElementReferenceException on dress_category_button click, retrying ({attempt+1}/{retries})")
        raise Exception("Failed to click 'Dress' category button due to repeated StaleElementReferenceException.")

    def click_on_dress_tile(self, retries=3):
        """Clicks the specific dress tile (product details page link)."""
        for attempt in range(retries):
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.dress_tile)
                ).click()
                return
            except StaleElementReferenceException:
                print(f"[WARNING] StaleElementReferenceException on dress_tile click, retrying ({attempt+1}/{retries})")
        raise Exception("Failed to click 'Dress' tile due to repeated StaleElementReferenceException.")
