import pytest

class TestMagentoShirtPurchase:
    def test_shirt_purchase(self, test_obj):
        page = test_obj
        try:
            page.login()
            page.search_and_add_shirt()
            page.proceed_to_checkout()
            page.fill_shipping_details()
            page.place_order()
        except Exception as e:
            page.driver.save_screenshot("test_failed.png")
            raise e
