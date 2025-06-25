from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from core_helpers.web_app_helper import Web_App_Helper
import SearchConfig
import os

class MagentoShirtPage(Web_App_Helper):
    def __init__(self, base_url=None):
        super().__init__(base_url=base_url)
        self.wait = WebDriverWait(self.driver, 20)

    def login(self):
        self.write("\n Navigating to login page")
        self.driver.get(SearchConfig.LOGIN_URL)
        self.wait.until(EC.presence_of_element_located((By.ID, SearchConfig.SIGN_IN_EMAIL_INPUT))).send_keys(os.getenv("EMAIL"))
        self.driver.find_element(By.ID, SearchConfig.SIGN_IN_PASSWORD_INPUT).send_keys(os.getenv("PASSWORD"))
        self.driver.find_element(By.ID, SearchConfig.SIGN_IN_BUTTON).click()
        self.wait.until(EC.presence_of_element_located((By.ID, SearchConfig.SEARCH_INPUT_ID)))
        self.write(" Logged in")

    def search_and_add_shirt(self):
        self.write("\n Searching for shirt")
        search_box = self.wait.until(EC.presence_of_element_located((By.ID, SearchConfig.SEARCH_INPUT_ID)))
        search_box.clear()
        search_box.send_keys("shirt")
        search_box.submit()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, SearchConfig.RADIANT_TEE_XPATH))).click()
        self.driver.execute_script("window.scrollBy(0, 500);")
        self.wait.until(EC.element_to_be_clickable((By.ID, SearchConfig.SIZE_M_ID))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, SearchConfig.COLOR_BLUE_ID))).click()
        add_to_cart_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, SearchConfig.ADD_TO_CART_XPATH)))
        self.driver.execute_script("arguments[0].click();", add_to_cart_btn)
        self.write(" Product added to cart")

    def proceed_to_checkout(self):
        self.write("\n Proceeding to checkout")
        cart_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, SearchConfig.CART_ICON_XPATH)))
        self.driver.execute_script("arguments[0].click();", cart_icon)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "minicart-items")))
        checkout_btn = self.wait.until(EC.element_to_be_clickable((By.ID, SearchConfig.MINICART_CHECKOUT_BUTTON_ID)))
        self.driver.execute_script("arguments[0].click();", checkout_btn)
        self.write(" Checkout initiated")

    def fill_shipping_details(self):
        self.write("\n Filling shipping details")
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
        self.write(" Shipping details submitted")

    def place_order(self):
        self.write("\n Placing the order")
        self.wait.until(EC.url_contains("checkout/#payment"))
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "img[alt='Loading...']")))
        place_order_btn = self.wait.until(EC.element_to_be_clickable(SearchConfig.PLACE_ORDER_BUTTON_XPATH))
        self.driver.execute_script("arguments[0].click();", place_order_btn)

        try:
            self.wait.until(EC.url_to_be(SearchConfig.SUCCESS_PAGE_URL))
            self.write(" Order placed successfully!")
        except:
            self.write(" Order placement failed")
            self.driver.save_screenshot("order_failure.png")
            assert False, "Order did not complete successfully"
