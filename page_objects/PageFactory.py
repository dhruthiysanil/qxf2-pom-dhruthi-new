# pylint: disable=import-outside-toplevel, E0401
from conf import base_url_conf as url_conf

class PageFactory():
    "PageFactory uses the factory design pattern."

    @staticmethod
    def get_page_object(page_name, base_url=url_conf.ui_base_url, driver=None):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()

        if page_name in ["zero", "zero page", "agent zero"]:
            from page_objects.zero_page import Zero_Page
            test_obj = Zero_Page(base_url=base_url)

        elif page_name == "magento login search":
            from page_objects.Magento_Login_Search import Magento_Login_Search
            test_obj = Magento_Login_Search(base_url=base_url)

        elif page_name == "magento login page":
            from page_objects.magento_login_page import MagentoLoginPage
            test_obj = MagentoLoginPage(driver=driver, base_url=base_url)
        else:
            raise Exception(f"Unknown page object: {page_name}")

        return test_obj
