# config/WomenConfig.py

from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

# URLs
HOME_URL = "https://magento.softwaretestingboard.com/"
LOGIN_URL = "https://magento.softwaretestingboard.com/customer/account/login/"
SUCCESS_PAGE_URL = "https://magento.softwaretestingboard.com/checkout/onepage/success/"

# Credentials from environment
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Login selectors
SIGN_IN_EMAIL_INPUT = "email"
SIGN_IN_PASSWORD_INPUT = "pass"
SIGN_IN_BUTTON = "send2"

# Search Product: Radiant Tee
SEARCH_INPUT_ID = "search"
RADIANT_TEE_XPATH = "//a[@class='product-item-link' and contains(text(), 'Radiant Tee')]"
SIZE_M_ID = "option-label-size-143-item-168"
COLOR_BLUE_ID = "option-label-color-93-item-50"
ADD_TO_CART_XPATH = "//button[@title='Add to Cart']/span[text()='Add to Cart']"

# Cart & Checkout Buttons
# Use actual <a> that opens cart, then <button> that triggers checkout
CART_ICON_XPATH = "//a[@class='action showcart']"  # Updated as per your HTML
MY_CART_XPATH = "//span[text()='My Cart']"
MINICART_CHECKOUT_BUTTON_ID = "top-cart-btn-checkout"

# Checkout Fields
CHECKOUT_COMPANY_SELECTOR = (By.NAME, "company")
CHECKOUT_STREET_SELECTOR = (By.NAME, "street[0]")
CHECKOUT_CITY_SELECTOR = (By.NAME, "city")
CHECKOUT_STATE_DROPDOWN_SELECTOR = (By.NAME, "region_id")
CHECKOUT_ZIP_SELECTOR = (By.NAME, "postcode")
CHECKOUT_COUNTRY_SELECTOR = (By.NAME, "country_id")
CHECKOUT_PHONE_SELECTOR = (By.NAME, "telephone")


# Checkout Shipping Info
COMPANY_NAME = "NethraTech Pvt Ltd"
STREET_ADDRESS = "123 AI Street"
CITY = "Bangalore"
STATE_INDEX = 1               # Index of the state in the dropdown
ZIP_CODE = "560001"
COUNTRY_INDEX = 1             # Index of the country in the dropdown
PHONE_NUMBER = "9844543210"


# Shipping & Payment
SHIPPING_METHOD_RADIO_XPATH = (By.XPATH, "//input[@type='radio' and contains(@value,'flatrate')]")
NEXT_BUTTON_XPATH = (By.XPATH, "//span[@data-bind=\"i18n: 'Next'\"]")
PLACE_ORDER_BUTTON_XPATH = (By.XPATH, "//span[@data-bind=\"i18n: 'Place Order'\"]")
