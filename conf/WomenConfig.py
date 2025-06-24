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

# Registration selectors
CREATE_ACCOUNT_LINK = "//a[contains(@href, 'customer/account/create')]"
FIRST_NAME_INPUT = "firstname"
LAST_NAME_INPUT = "lastname"
EMAIL_INPUT = "email_address"
PASSWORD_INPUT = "password"
CONFIRM_PASSWORD_INPUT = "password-confirmation"
CREATE_ACCOUNT_BUTTON = "//button[@title='Create an Account']"
