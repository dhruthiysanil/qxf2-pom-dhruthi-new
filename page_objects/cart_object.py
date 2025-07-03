
"""
Cart object which will open the cart section
"""

import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Cart_Object:
    "Cart object for Magento site"

    # Locators
    cart_icon = locators.cart_icon                 
    proceed_to_checkout_button = locators.proceed_to_checkout_button  # id,top-cart-btn-checkout

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def open_cart(self):
        "Click on the cart icon to open mini cart"
        result_flag = self.click_element(self.cart_icon)
        self.conditional_write(result_flag,
            positive='Clicked on the Cart icon to open mini cart',
            negative='Failed to click Cart icon',
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def proceed_to_checkout(self):
        "Click on the Proceed to Checkout button"
        result_flag = self.click_element(self.proceed_to_checkout_button)
        self.conditional_write(result_flag,
            positive='Clicked Proceed to Checkout',
            negative='Failed to click Proceed to Checkout',
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def complete_cart_flow(self):
        "Cart flow: open cart and proceed to checkout"
        result_flag = self.open_cart()
        if result_flag:
            self.wait(2)
        result_flag &= self.proceed_to_checkout()

        # Switch to shipping page if successful
        if result_flag:
            self.switch_page("shipping page")

        self.conditional_write(result_flag,
            positive='Cart flow completed: Proceeded to checkout',
            negative='Cart flow failed',
            level='debug')
        return result_flag
