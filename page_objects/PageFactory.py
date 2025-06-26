"""
PageFactory uses the Factory Design Pattern.
get_page_object() returns the appropriate page object based on the page_name argument.

Pages implemented so far:
1. Zero Page
2. Zero Mobile Page
3. Magento Shirt Page
4. Register Page
5. Login Page

Add additional elif clauses as you implement more pages.
"""

# pylint: disable=import-outside-toplevel, E0401
from conf import base_url_conf as url_conf

class PageFactory():
    "PageFactory uses the factory design pattern."
    
    @staticmethod
    def get_page_object(page_name, base_url=url_conf.ui_base_url):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()

        if page_name in ["zero", "zero page", "agent zero"]:
            from page_objects.zero_page import Zero_Page
            test_obj = Zero_Page(base_url=base_url)

        elif page_name in ["zero mobile", "zero mobile page"]:
            from page_objects.zero_mobile_page import Zero_Mobile_Page
            test_obj = Zero_Mobile_Page()

        elif page_name == "magento shirt page":
            from page_objects.MagentoShirtPage import MagentoShirtPage
            test_obj = MagentoShirtPage(base_url=base_url)

        elif page_name in ["register page", "registration page"]:
            from page_objects.register_page import RegisterPage
            test_obj = RegisterPage(base_url)

        elif page_name in ["login page", "sign in page"]:
            from page_objects.login_page import LoginPage
            test_obj = LoginPage(base_url)

        # Add more page objects below as needed...

        return test_obj
