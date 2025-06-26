from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

# ----------------------- URLs -----------------------
HOME_URL = "https://magento.softwaretestingboard.com/"
LOGIN_URL = "https://magento.softwaretestingboard.com/customer/account/login/"
SUCCESS_PAGE_URL = "https://magento.softwaretestingboard.com/checkout/onepage/success/"

# -------------------- Credentials --------------------
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# ------------------ Login Selectors ------------------
SIGN_IN_EMAIL_INPUT = (By.ID, "email")
SIGN_IN_PASSWORD_INPUT = (By.ID, "pass")
SIGN_IN_BUTTON = (By.ID, "send2")

# ------------------- Search Field --------------------
SEARCH_BAR = (By.ID, "search")

# ---------------- Radiant Tee Page -------------------
SIZE_SELECTOR = (By.ID, "option-label-size-143-item-167")     # Size: S
COLOR_SELECTOR = (By.ID, "option-label-color-93-item-50")     # Color: Blue
ADD_TO_CART_BUTTON = (By.ID, "product-addtocart-button")

# ------------------ Cart Selectors -------------------
CART_ICON = (By.CSS_SELECTOR, "a.action.showcart")
CART_TEXT = (By.CSS_SELECTOR, "span.text")
PROCEED_TO_CHECKOUT_BUTTON = (By.ID, "top-cart-btn-checkout")

# ------------ Checkout Shipping Info -----------------
COMPANY_NAME = "NethraTech Pvt Ltd"
STREET_ADDRESS = "123 AI Street"
CITY = "Bangalore"
STATE_INDEX = 1
ZIP_CODE = "560001"
COUNTRY_INDEX = 1
PHONE_NUMBER = "9844543210"

# ----------- Shipping Page Selectors -----------------
CHECKOUT_COMPANY_SELECTOR = (By.NAME, "company")
CHECKOUT_STREET_SELECTOR = (By.NAME, "street[0]")
CHECKOUT_CITY_SELECTOR = (By.NAME, "city")
CHECKOUT_STATE_DROPDOWN_SELECTOR = (By.NAME, "region_id")
CHECKOUT_ZIP_SELECTOR = (By.NAME, "postcode")
CHECKOUT_COUNTRY_SELECTOR = (By.NAME, "country_id")
CHECKOUT_PHONE_SELECTOR = (By.NAME, "telephone")

# -------------- Shipping & Payment -------------------
SHIPPING_METHOD_RADIO_XPATH = (By.XPATH, "//input[@type='radio' and contains(@value,'flatrate')]")
NEXT_BUTTON_XPATH = (By.XPATH, "//span[@data-bind=\"i18n: 'Next'\"]")
PLACE_ORDER_BUTTON_XPATH = (By.XPATH, "//span[@data-bind=\"i18n: 'Place Order'\"]")
