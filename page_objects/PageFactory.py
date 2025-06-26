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

        elif page_name == "magento shirt page":
            from page_objects.magento_shirt_page import MagentoShirtPage
            test_obj = MagentoShirtPage(driver=driver)

        elif page_name in ["register page", "registration page"]:
            from page_objects.register_page import RegisterPage
            test_obj = RegisterPage(driver=driver)

        elif page_name == "login page":
            from page_objects.Magento.login_page import LoginPage
            test_obj = LoginPage(driver=driver)

        elif page_name == "cart page":
            from page_objects.Magento.cart_page import CartPage
            test_obj = CartPage(driver=driver)

        elif page_name == "shipping page":
            from page_objects.Magento.shipping_page import ShippingPage
            test_obj = ShippingPage(driver=driver)

        return test_obj
