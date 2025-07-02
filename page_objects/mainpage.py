'''THis is the MainPage which handles login object'''

from core_helpers.web_app_helper import Web_App_Helper
from page_objects.login_object import Login_Object

class Main_Page(Web_App_Helper, Login_Object):
    "Page Object for the Magento main page (login)"

    def start(self):
        "Use this method to go to the Magento home page"
        self.open("/")
