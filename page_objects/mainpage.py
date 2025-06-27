"""
This class models the Magento main page.
URL: https://magento.softwaretestingboard.com/
The page consists of a login page object (for authentication flows).
"""

from core_helpers.web_app_helper import Web_App_Helper
from page_objects.login_object import Login_Object  # Use your actual login object

class Magento_Main_Page(Web_App_Helper, Login_Object):
    "Page Object for the Magento main page"

    def start(self):
        "Use this method to go to the Magento home page"
        self.open("/") 
