'''Search Object which willl search shirt and click on size and color'''

import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Search_Object:
    # "Search object for Magento site"

    # Locators
    search_box = locators.search_box
    product_image = locators.product_circe_image
    size_option = locators.size_s
    color_option = locators.color_green
    add_to_cart_button = locators.add_to_cart_button

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def search_for_product(self, product_name):
        # "Enter product name in search box and press Enter"
        result_flag = self.set_text(self.search_box, product_name)
        self.hit_enter(self.search_box)

        self.conditional_write(result_flag,
            positive=f"Searched for product: {product_name}",
            negative="Failed to search product",
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_product(self):
        # "Scroll to and click on Circe Hooded Ice Fleece image"
        scroll_flag = self.scroll_down(self.product_image)  # updated from scroll_to_element
        result_flag = False
        if scroll_flag:
            result_flag = self.click_element(self.product_image)

        self.conditional_write(result_flag,
            positive="Clicked on product image (Circe Hooded Ice Fleece)",
            negative="Failed to click product image",
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_size(self):
        # "Select size S"
        result_flag = self.click_element(self.size_option)
        self.conditional_write(result_flag,
            positive="Selected size S",
            negative="Failed to select size S",
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_color(self):
        # "Select color Green"
        result_flag = self.click_element(self.color_option)
        self.conditional_write(result_flag,
            positive="Selected color Green",
            negative="Failed to select color Green",
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_add_to_cart(self):
        # "Click on Add to Cart button"
        result_flag = self.click_element(self.add_to_cart_button)
        self.conditional_write(result_flag,
            positive="Clicked Add to Cart",
            negative="Failed to click Add to Cart",
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def search_and_add_product(self, product_name="shirt"):
        # "Search, click product image, select size/color, and add to cart"
        result_flag = self.search_for_product(product_name)
        result_flag &= self.click_product()
        result_flag &= self.select_size()
        result_flag &= self.select_color()
        result_flag &= self.click_add_to_cart()

        self.conditional_write(result_flag,
            positive="Successfully added product to cart",
            negative="Failed to add product to cart",
            level='debug')
        return result_flag
