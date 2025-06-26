"""
test_magento_add_shirt.py

This test automates the flow of purchasing a shirt on the Magento site.
Steps:
- Logging in with credentials
- Searching for a product (Radiant Tee)
- Selecting size and color
- Adding product to cart
- Proceeding to checkout
- Filling shipping details
- Placing the order
- Verifying success page

Uses PageFactory to fetch page objects and logs each step with test_obj.
"""

import os
import sys
import time
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from conf import SearchConfig

@pytest.mark.GUI
def test_magento_purchase_flow(test_obj):
    "Login, add Radiant Tee to cart, and complete checkout"

    try:
        expected_pass = 0
        actual_pass = -1
        start_time = int(time.time())

        email = SearchConfig.EMAIL
        password = SearchConfig.PASSWORD
        if not email or not password:
            pytest.fail("EMAIL or PASSWORD not set in environment or SearchConfig")

        # Load login, cart, and shipping pages
        login_page = PageFactory.get_page_object("login page", driver=test_obj.driver)
        cart_page = PageFactory.get_page_object("cart page", driver=test_obj.driver)
        shipping_page = PageFactory.get_page_object("shipping page", driver=test_obj.driver)

        # Login
        test_obj.log_result(login_page.load_login_page(), "Login page loaded", "Failed to load login page")
        test_obj.log_result(login_page.enter_credentials(email, password), "Entered credentials", "Failed to enter credentials")
        test_obj.log_result(login_page.submit_login(), "Submitted login", "Failed to submit login")

        # Search
        test_obj.log_result(login_page.redirect_to_women_page(), "Redirected to Women page", "Redirect failed")
        test_obj.log_result(login_page.search_for_product("shirt"), "Searched product", "Search failed")
        test_obj.log_result(login_page.click_radiant_tee(), "Radiant Tee opened", "Failed to open product")

        # Cart flow
        test_obj.log_result(cart_page.select_size_and_color(), "Size & color selected", "Failed to select size/color")
        test_obj.log_result(cart_page.add_to_cart(), "Added to cart", "Add to cart failed")
        test_obj.log_result(cart_page.go_to_cart(), "Opened cart", "Failed to open cart")
        test_obj.log_result(cart_page.proceed_to_checkout(), "Checkout initiated", "Checkout failed")

        # Shipping + Order
        test_obj.log_result(shipping_page.fill_shipping_details(), "Shipping details filled", "Failed to fill shipping info")
        test_obj.log_result(shipping_page.place_order(), "Order placed", "Order failed")
        test_obj.log_result(shipping_page.check_order_success(), "Reached success page", "Not on success page")

        # Summary
        test_obj.write(f"\nTest completed in {int(time.time() - start_time)} seconds\n")
        test_obj.write(f"Checks passed: {test_obj.pass_counter} / {test_obj.result_counter}")
        test_obj.write_test_summary()

        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter

    except Exception as e:
        print(f"Exception occurred in test: {__file__}")
        print(f"Error: {str(e)}")
        test_obj.write(f"Exception: {e}")
        test_obj.write_test_summary()

    assert expected_pass == actual_pass, f"Test failed: {__file__} | Passed {actual_pass} of {expected_pass}"
