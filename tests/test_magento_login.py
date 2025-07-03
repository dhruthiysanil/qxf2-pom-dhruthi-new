
"""
Automated test using Qxf2's framework for Magento:
    1. Login to Magento.
    2. Search for a product.
    3. Select size/color and add to cart.
    4. Proceed to checkout using cart.
    5. Complete the shipping and place the order.
"""

import pytest
import time
from page_objects.PageFactory import PageFactory
import conf.magento_conf as conf
from conf.shipping_info import shipping_data  

@pytest.mark.GUI
def test_magento_login_and_checkout_flow(test_obj):
    "Magento login, product selection, and order flow"

    try:
        expected_pass = 0
        actual_pass = -1
        start_time = int(time.time())

        email = conf.email
        password = conf.password
        product_name = conf.product

        # Step 1: Open Main Page
        test_obj = PageFactory.get_page_object("Main Page", base_url=test_obj.base_url)

        # Step 2: Login
        result_flag = test_obj.login_to_magento(email, password)
        test_obj.log_result(result_flag,
            positive=f"Logged in successfully with email: {email}",
            negative=f"Login failed for email: {email}")

        # Step 3: Search for product
        result_flag &= test_obj.search_for_product(product_name)
        test_obj.log_result(result_flag,
            positive=f"Searched for product: {product_name}",
            negative=f"Failed to search for product: {product_name}")

        # Step 4: Select size, color, add to cart
        result_flag &= test_obj.select_and_add_product()
        test_obj.log_result(result_flag,
            positive=f"Selected options and added '{product_name}' to cart",
            negative=f"Failed to add '{product_name}' to cart")

        # Step 5: Proceed to checkout
        result_flag &= test_obj.complete_cart_flow()
        test_obj.log_result(result_flag,
            positive="Proceeded to checkout successfully",
            negative="Failed to proceed to checkout")

        # Step 6: Complete shipping and place order
        if result_flag:
            test_obj = PageFactory.get_page_object("Shipping Page", base_url=test_obj.base_url)
            result_flag &= test_obj.complete_shipping_flow(shipping_data)
            test_obj.log_result(result_flag,
                positive="Shipping form submitted and order placed successfully",
                negative="Shipping form submission or order placement failed")

        # Final log and result
        test_obj.write(f'Script duration: {int(time.time() - start_time)} seconds\n')
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter

    except Exception as e:
        print(f"Exception during test: {__file__}")
        print(f"Python says: {str(e)}")

    assert expected_pass == actual_pass, f"Test failed: {__file__}"
