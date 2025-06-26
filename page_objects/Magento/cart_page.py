# File: page_objects/Magento/cart_page.py

    # Page object for product selection and cart actions:
    # - Select size and color
    # - Add to cart
    # - Proceed to checkout


import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from conf import SearchConfig
from utils.Wrapit import Wrapit

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.screenshot_counter = 1
        self.current_console_log_errors = []

    def save_screenshot(self, name):
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        self.driver.save_screenshot(f"screenshots/{name}.png")

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def select_size_and_color(self):
        """Select size and color of the product"""
        size_elem = self.wait.until(EC.element_to_be_clickable(SearchConfig.SIZE_SELECTOR))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", size_elem)
        size_elem.click()

        color_elem = self.wait.until(EC.element_to_be_clickable(SearchConfig.COLOR_SELECTOR))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", color_elem)
        color_elem.click()
        return True

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def add_to_cart(self):
        """Click 'Add to Cart' button"""
        add_btn = self.wait.until(EC.element_to_be_clickable(SearchConfig.ADD_TO_CART_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_btn)
        add_btn.click()
        return True

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def go_to_cart(self):
        """Click the cart icon to open cart"""
        cart_icon = self.wait.until(EC.element_to_be_clickable(SearchConfig.CART_ICON))
        cart_icon.click()
        self.wait.until(EC.visibility_of_element_located(SearchConfig.CART_TEXT))
        return True

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def proceed_to_checkout(self):
        """Click 'Proceed to Checkout' button"""
        checkout_btn = self.wait.until(EC.element_to_be_clickable(SearchConfig.PROCEED_TO_CHECKOUT_BUTTON))
        checkout_btn.click()
        return True
