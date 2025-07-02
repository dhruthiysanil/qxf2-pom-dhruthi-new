'''This is the landing page which has search object and cart object'''
from core_helpers.web_app_helper import Web_App_Helper
from page_objects.search_object import Search_Object
from page_objects.cart_object import Cart_Object

class Landing_Page(Web_App_Helper, Search_Object, Cart_Object):
    "Page Object for the Magento landing page with search and cart features"

    def start(self):
        "Use this method to go to the Magento home page"
        self.open("/")
