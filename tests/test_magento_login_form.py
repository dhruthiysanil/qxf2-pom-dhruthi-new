import pytest
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

from page_objects.magento_login_page import MagentoLoginPage
from conf.magento_conf import MagentoConf

load_dotenv()

@pytest.mark.GUI
def test_magento_login(test_obj):
    """
    Qxf2-style test to perform login on the Magento website.
    """
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    conf = MagentoConf()

    if not email or not password:
        pytest.fail("EMAIL or PASSWORD not set in the .env file")

    # Initialize the page object
    login_page = MagentoLoginPage(test_obj.driver, base_url=conf.base_url)

    # Step 1: Navigate to login page
    login_page.go_to()

    # Step 2: Fill in login details and submit
    login_page.set_email(email)
    login_page.set_password(password)
    login_page.submit_login()

    # Step 3: Verify login success
    result_flag = login_page.check_login_success()
    if not result_flag:
        try:
            error_msg = login_page.get_error_message()
            print("Login error message:", error_msg)
        except:
            print("No visible error message found.")

    login_page.log_result(result_flag,
                          positive="Login test passed.",
                          negative="Login test failed.")

    login_page.write_test_summary()
