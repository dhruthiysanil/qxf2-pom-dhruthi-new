"""
Magento Login Test using Qxf2's framework.
Steps:
    1. Open Magento homepage.
    2. Click on 'Sign In'.
    3. Enter email and password from environment.
    4. Click Sign In button.
    5. Verify login success.
    6. Redirect to Women section.
"""

import os
import sys
import time
import pytest
from dotenv import load_dotenv

# Add root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from page_objects.PageFactory import PageFactory  # Qxf2 Page Object Factory

# Load credentials from .env
load_dotenv()

@pytest.mark.GUI
def test_magento_login(test_obj):
    "Magento login and redirect to Women section using Qxf2"

    try:
        expected_pass = 0
        actual_pass = -1
        start_time = int(time.time())

        # Step 1: Load email and password from .env
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")
        if not email or not password:
            pytest.fail("EMAIL or PASSWORD not set in .env file")

        # Step 2: Load Main Page object from Qxf2 PageFactory
        test_obj = PageFactory.get_page_object("Main Page")
        test_obj.start()

        # Step 3–6: Perform login + redirect to Women section
        result_flag = test_obj.login_to_magento(email, password)

        # Step 7: Log result
        test_obj.log_result(
            result_flag,
            positive="Successfully logged in and navigated to Women section\n",
            negative="Login or redirection to Women section failed\nURL: %s\n" % test_obj.get_current_url(),
            level="critical"
        )

        # Step 8: Report script duration
        script_duration = int(time.time()) - start_time
        test_obj.write("Script duration: %d seconds\n" % script_duration)

        # Step 9: Add Tesults report (optional integration)
        test_obj.add_tesults_case(
            "Magento Login + Redirect",
            "Login & navigate to Women section",
            "test_magento_login",
            result_flag,
            "Redirection failed\nURL: %s\n" % test_obj.get_current_url(),
            []
        )

        # Step 10: Final summary
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter

    except Exception as e:
        print("Exception during test: %s" % __file__)
        print("Python says: %s" % str(e))

    # Final assertion
    assert expected_pass == actual_pass, "Test failed: %s" % __file__
