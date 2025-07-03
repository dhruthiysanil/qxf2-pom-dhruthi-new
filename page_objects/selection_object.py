
'''Handles selecting a shirt product, size, color, and adding to cart'''
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Selection_Object:
    product_image = locators.product_circe_image
    size_option = locators.size_s
    color_option = locators.color_green
    add_to_cart_button = locators.add_to_cart_button

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_product(self):
        "Click on the shirt product image"
        scroll_flag = self.scroll_down(self.product_image)
        result_flag = False
        if scroll_flag:
            result_flag = self.click_element(self.product_image)
        self.conditional_write(result_flag, "Clicked product image", "Failed to click product image", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_size(self):
        "Select size"
        result_flag = self.click_element(self.size_option)
        self.conditional_write(result_flag, "Selected size S", "Failed to select size S", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_color(self):
        "Select color"
        result_flag = self.click_element(self.color_option)
        self.conditional_write(result_flag, "Selected color Green", "Failed to select color Green", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_add_to_cart(self):
        "Click on Add to Cart"
        result_flag = self.click_element(self.add_to_cart_button)
        self.conditional_write(result_flag, "Clicked Add to Cart", "Failed to click Add to Cart", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_and_add_product(self):
        "Click shirt, select size, color and add to cart"
        result_flag = self.click_product()
        result_flag &= self.select_size()
        result_flag &= self.select_color()
        result_flag &= self.click_add_to_cart()

        self.conditional_write(result_flag,
            positive="Successfully selected shirt, size, color and added to cart",
            negative="Failed during product selection or add to cart",
            level='debug')
        return result_flag
