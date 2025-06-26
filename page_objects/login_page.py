"""
LoginPage.py

This module contains the LoginPage class that automates login, product search,
selection, and checkout flow on the Magento site using Selenium WebDriver.
It is part of the Qxf2 automation framework and uses locators from SearchConfig.
"""

import os
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.Wrapit import Wrapit
from conf import SearchConfig


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.screenshot_counter = 1
        self.current_console_log_errors = []

    def save_screenshot(self, name):
        "Helper to save screenshot with proper path"
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        self.driver.save_screenshot(f"screenshots/{name}.png")

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def load_login_page(self):
        self.driver.get(SearchConfig.LOGIN_URL)
        return "login" in self.driver.current_url

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def enter_credentials(self, email, password):
        self.wait.until(EC.visibility_of_element_located(SearchConfig.SIGN_IN_EMAIL_INPUT)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(SearchConfig.SIGN_IN_PASSWORD_INPUT)).send_keys(password)
        return True

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def submit_login(self):
        self.wait.until(EC.element_to_be_clickable(SearchConfig.SIGN_IN_BUTTON)).click()
        return True

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def redirect_to_women_page(self):
        self.driver.get(f"{SearchConfig.HOME_URL}women.html")
        return self.wait.until(EC.visibility_of_element_located(SearchConfig.SEARCH_BAR)) is not None

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def search_for_product(self, product):
        search_input = self.wait.until(EC.visibility_of_element_located(SearchConfig.SEARCH_BAR))
        search_input.clear()
        search_input.send_keys(product)
        search_input.submit()
        return True

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_radiant_tee(self):
        self.driver.get(f"{SearchConfig.HOME_URL}radiant-tee.html")
        return "radiant-tee" in self.driver.current_url

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def select_size_and_color(self):
        print("Waiting for size S to be clickable...")
        size_elem = self.wait.until(EC.element_to_be_clickable(SearchConfig.SIZE_SELECTOR))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", size_elem)
        size_elem.click()
        print("Size S selected.")

        print("Waiting for color Blue to be clickable...")
        color_elem = self.wait.until(EC.element_to_be_clickable(SearchConfig.COLOR_SELECTOR))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", color_elem)
        color_elem.click()
        print("Color Blue selected.")
        return True

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def add_to_cart(self):
        print("Waiting for Add to Cart button...")
        add_btn = self.wait.until(EC.element_to_be_clickable(SearchConfig.ADD_TO_CART_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_btn)
        add_btn.click()
        print("Product added to cart.")
        return True

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def go_to_cart(self):
        print("Opening My Cart...")
        cart_icon = self.wait.until(EC.element_to_be_clickable(SearchConfig.CART_ICON))
        cart_icon.click()
        self.wait.until(EC.visibility_of_element_located(SearchConfig.CART_TEXT))
        print("My Cart opened.")
        return True

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def proceed_to_checkout(self):
        print("Proceeding to checkout...")
        checkout_btn = self.wait.until(EC.element_to_be_clickable(SearchConfig.PROCEED_TO_CHECKOUT_BUTTON))
        checkout_btn.click()
        print("Proceed to Checkout clicked.")
        return True

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def fill_shipping_details(self):
        print("Filling shipping details...")
        self.wait.until(EC.url_contains("checkout/#shipping"))

        self.wait.until(EC.presence_of_element_located(SearchConfig.CHECKOUT_COMPANY_SELECTOR)).send_keys(SearchConfig.COMPANY_NAME)
        self.wait.until(EC.presence_of_element_located(SearchConfig.CHECKOUT_STREET_SELECTOR)).send_keys(SearchConfig.STREET_ADDRESS)
        self.wait.until(EC.presence_of_element_located(SearchConfig.CHECKOUT_CITY_SELECTOR)).send_keys(SearchConfig.CITY)
        Select(self.wait.until(EC.element_to_be_clickable(SearchConfig.CHECKOUT_STATE_DROPDOWN_SELECTOR))).select_by_index(SearchConfig.STATE_INDEX)
        self.wait.until(EC.presence_of_element_located(SearchConfig.CHECKOUT_ZIP_SELECTOR)).send_keys(SearchConfig.ZIP_CODE)
        Select(self.wait.until(EC.element_to_be_clickable(SearchConfig.CHECKOUT_COUNTRY_SELECTOR))).select_by_index(SearchConfig.COUNTRY_INDEX)
        self.wait.until(EC.presence_of_element_located(SearchConfig.CHECKOUT_PHONE_SELECTOR)).send_keys(SearchConfig.PHONE_NUMBER)

        self.wait.until(EC.element_to_be_clickable(SearchConfig.SHIPPING_METHOD_RADIO_XPATH)).click()
        self.wait.until(EC.element_to_be_clickable(SearchConfig.NEXT_BUTTON_XPATH)).click()
        print("Shipping info filled.")
        return True

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def place_order(self):
        print("Placing the order...")
        self.wait.until(EC.url_contains("checkout/#payment"))
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "img[alt='Loading...']")))

        place_btn = self.wait.until(EC.element_to_be_clickable(SearchConfig.PLACE_ORDER_BUTTON_XPATH))
        self.driver.execute_script("arguments[0].click();", place_btn)

        self.wait.until(EC.url_to_be(SearchConfig.SUCCESS_PAGE_URL))
        print("Order placed successfully!")
        return True

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_order_success(self):
        return SearchConfig.SUCCESS_PAGE_URL in self.driver.current_url
