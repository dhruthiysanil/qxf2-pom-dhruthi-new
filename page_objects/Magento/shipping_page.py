# File: page_objects/Magento/shipping_page.py
"""
ShippingPage class automates the checkout and shipping steps for the Magento shirt purchase flow.
Includes methods to:
- Fill in shipping details
- Place the order
- Verify if the success page is reached
"""

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from conf import SearchConfig
from utils.Wrapit import Wrapit

class ShippingPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Fill in all the required shipping information and proceed
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def fill_shipping_details(self):
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
        return True

    # Click on 'Place Order' and wait for the success page
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def place_order(self):
        self.wait.until(EC.url_contains("checkout/#payment"))
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "img[alt='Loading...']")))

        place_btn = self.wait.until(EC.element_to_be_clickable(SearchConfig.PLACE_ORDER_BUTTON_XPATH))
        self.driver.execute_script("arguments[0].click();", place_btn)

        self.wait.until(EC.url_to_be(SearchConfig.SUCCESS_PAGE_URL))
        return True

    # Verify the order success page was reached
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_order_success(self):
        return SearchConfig.SUCCESS_PAGE_URL in self.driver.current_url
