'''Handles shipping object'''
from core_helpers.web_app_helper import Web_App_Helper
from page_objects.shipping_object import Shipping_Object

class Shipping_Page(Web_App_Helper, Shipping_Object):
    "Page Object for Magento shipping and place order"

    def start(self):
        "Start should assume we are already at the shipping page from Search flow"
        # Do not navigate again – you're already at the correct shipping page
        # self.smart_wait(self.CHECKOUT_COMPANY_SELECTOR, wait_seconds=15)
        pass