"""
This is an example automated test to help you learn Qxf2's framework.
Our automated test will do the following:
    1. Open Magento homepage.
    2. Click on 'Sign In'.
    3. Enter email and password.
    4. Click Sign In button.
    5. Verify login success.
    6. Redirect to Women section.
    7. Search for 'shirt'.
    8. Click on 'Circe Hooded Ice Fleece'.
    9. Select size S.
    10. Select color Green.
    11. Add product to cart.
    12. Proceed to checkout from cart.
    13. Fill shipping form and place order.
"""

import os, sys, time, pytest
from dotenv import load_dotenv

# Add root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from page_objects.PageFactory import PageFactory

# Load credentials from .env
load_dotenv()

@pytest.mark.GUI
def test_magento_login_and_search(test_obj):
    "Magento login, search, add to cart, checkout, and shipping test using Qxf2 framework"

    try:
        # Initialize summary flags
        expected_pass = 0
        actual_pass = -1
        start_time = int(time.time())

        # Load credentials
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")
        if not email or not password:
            pytest.fail("EMAIL or PASSWORD not set in .env file")

        # Step 1: Create Main Page object
        test_obj = PageFactory.get_page_object("Main Page", base_url=test_obj.base_url)

        # Step 2: Click login link
        result_flag = test_obj.click_login_link()
        test_obj.log_result(result_flag,
                            positive="Clicked on login link successfully",
                            negative="Failed to click login link\nURL: %s" % test_obj.get_current_url())
        test_obj.add_tesults_case("Click Login Link", "Clicks the login link", "test_magento_login_and_search", result_flag, "", [])

        # Step 3: Set Email
        result_flag &= test_obj.set_email(email)
        test_obj.log_result(result_flag,
                            positive="Email set to: %s" % email,
                            negative="Failed to set email: %s\nURL: %s" % (email, test_obj.get_current_url()))
        test_obj.add_tesults_case("Set Email", "Enter email", "test_magento_login_and_search", result_flag, "", [])

        # Step 4: Set Password
        result_flag &= test_obj.set_password(password)
        test_obj.log_result(result_flag,
                            positive="Password was set successfully",
                            negative="Failed to set password\nURL: %s" % test_obj.get_current_url())
        test_obj.add_tesults_case("Set Password", "Enter password", "test_magento_login_and_search", result_flag, "", [])

        # Step 5: Click Sign In
        result_flag &= test_obj.click_sign_in()
        test_obj.log_result(result_flag,
                            positive="Clicked Sign In button",
                            negative="Failed to click Sign In button\nURL: %s" % test_obj.get_current_url())
        test_obj.add_tesults_case("Click Sign In", "Clicks sign in button", "test_magento_login_and_search", result_flag, "", [])

        # Step 6: Check login success
        result_flag &= test_obj.check_login_success()
        test_obj.log_result(result_flag,
                            positive="Login successful",
                            negative="Login failed\nURL: %s" % test_obj.get_current_url())
        test_obj.add_tesults_case("Check Login", "Verifies login", "test_magento_login_and_search", result_flag, "", [])

        # Step 7: Click Women section
        result_flag &= test_obj.click_women_section()
        test_obj.log_result(result_flag,
                            positive="Navigated to Women section",
                            negative="Failed to navigate to Women section\nURL: %s" % test_obj.get_current_url())
        test_obj.add_tesults_case("Women Section", "Navigate to Women section", "test_magento_login_and_search", result_flag, "", [])

        # Step 8–11: Search and add Circe product to cart
        result_flag &= test_obj.search_and_add_product("shirt")  # uses Circe image, size S, color Green inside method
        test_obj.log_result(result_flag,
                            positive="Successfully searched and added product to cart",
                            negative="Failed to search or add product to cart\nURL: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.add_tesults_case("Search & Add Product", "Search for shirt and add Circe product to cart", "test_magento_login_and_search", result_flag, "", [])

        # Step 12: Proceed to checkout
        result_flag &= test_obj.complete_cart_flow()
        test_obj.log_result(result_flag,
                            positive="Proceeded to checkout successfully",
                            negative="Failed to proceed to checkout\nURL: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.add_tesults_case("Checkout", "Open cart and proceed to checkout", "test_magento_login_and_search", result_flag, "", [])

        # Step 13: Fill shipping form and place order
        result_flag &= test_obj.complete_shipping_flow()
        test_obj.log_result(result_flag,
                            positive="Filled shipping info and placed order",
                            negative="Failed during shipping or placing order\nURL: %s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.add_tesults_case("Shipping & Order", "Fills shipping form and places order", "test_magento_login_and_search", result_flag, "", [])

        # Script duration
        test_obj.write('Script duration: %d seconds\n' % (int(time.time() - start_time)))

        # Write final test summary
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter

    except Exception as e:
        print("Exception during test: %s" % __file__)
        print("Python says: %s" % str(e))

    # Final assertion
    assert expected_pass == actual_pass, "Test failed: %s" % __file__
