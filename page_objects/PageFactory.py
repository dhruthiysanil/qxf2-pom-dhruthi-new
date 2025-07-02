from conf import base_url_conf as url_conf

class PageFactory:
    "PageFactory uses the factory design pattern."

    @staticmethod
    def get_page_object(page_name, driver=None, base_url=url_conf.ui_base_url):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()

        if page_name in ["zero", "zero page", "agent zero"]:
            from page_objects.zero_page import Zero_Page
            test_obj = Zero_Page(base_url=base_url)

        elif page_name in ["zero mobile", "zero mobile page"]:
            from page_objects.zero_mobile_page import Zero_Mobile_Page
            test_obj = Zero_Mobile_Page()

        # elif page_name in ["login", "login page"]:
        #     from page_objects.login_page import LoginPage
        #     test_obj = LoginPage(driver=driver)

        # elif page_name in ["cart", "cart page"]:
        #     from page_objects.cart_page import CartPage
        #     test_obj = CartPage(driver=driver)

        elif page_name in ["main", "main page"]:
            from page_objects.mainpage import Main_Page
            test_obj = Main_Page(base_url=base_url)

        elif page_name in ["landing", "landing page"]:
            from page_objects.landing_page import Landing_Page
            test_obj = Landing_Page(base_url=base_url)

        elif page_name in ["shipping", "shipping page"]:
            from page_objects.shipping_page import Shipping_Page
            test_obj = Shipping_Page(base_url=base_url) 

        if test_obj is None:
            raise Exception(f"PageFactory: No matching page found for '{page_name}'")

        return test_obj
