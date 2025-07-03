"""
Automated test using Qxf2's framework for Magento:
    1. Login to Magento.
    2. Search for a product and add to cart.
    3. Complete the shipping and place the order.
"""

from page_objects.PageFactory import PageFactory
import pytest
import time
import conf.magento_conf as conf

@pytest.mark.GUI
def test_magento_login_and_search(test_obj):
    "Magento login, search, checkout and shipping flow"

    try:
        # Initialize result tracking
        expected_pass = 0
        actual_pass = -1
        start_time = int(time.time())

        # Load credentials
        email = conf.email
        password = conf.password
        product_name = "shirt"

        # Step 1: Open Main Page
        test_obj = PageFactory.get_page_object("Main Page", base_url=test_obj.base_url)

        # Step 2: Login
        result_flag = test_obj.login_to_magento(email, password)
        test_obj.log_result(result_flag,
                            positive=f"Logged in successfully with email: {email}",
                            negative=f"Login failed for email: {email}")

        # Step 3: Search and Add Product
        result_flag &= test_obj.search_and_add_product(product_name)
        test_obj.log_result(result_flag,
                            positive=f"Searched for and added '{product_name}' to cart",
                            negative=f"Failed to add '{product_name}' to cart")

        # Step 4: Complete shipping and place order
        if result_flag:
            test_obj = PageFactory.get_page_object("Shipping Page", base_url=test_obj.base_url)
            result_flag &= test_obj.complete_shipping_flow()
            test_obj.log_result(result_flag,
                                positive="Shipping form submitted and order placed successfully",
                                negative="Shipping form submission or order placement failed")

        # Wrap up
        test_obj.write('Script duration: %d seconds\n' % (int(time.time() - start_time)))
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter

    except Exception as e:
        print(f"Exception during test: {__file__}")
        print(f"Python says: {str(e)}")

    assert expected_pass == actual_pass, f"Test failed: {__file__}"
