"""
This class models the Magento main page.
URL: https://magento.softwaretestingboard.com/
The page consists of login, search, cart, and shipping page objects.
"""

from core_helpers.web_app_helper import Web_App_Helper
from page_objects.login_object import Login_Object
from page_objects.search_object import Search_Object
from page_objects.cart_object import Cart_Object
from page_objects.shipping_object import Shipping_Object  # ✅ Import shipping

class Magento_Main_Page(Web_App_Helper, Login_Object, Search_Object, Cart_Object, Shipping_Object):
    # "Page Object for the Magento main page"

    def start(self):
        "Use this method to go to the Magento home page"
        self.open("/") 
        # "Use this method to go to the Magento home page"
        self.open("/")

