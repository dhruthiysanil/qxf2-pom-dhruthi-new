'''Search object is used to search shirt '''
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Search_Object:
    search_box = locators.search_box
    product_image = locators.product_circe_image
    size_option = locators.size_s
    color_option = locators.color_green
    add_to_cart_button = locators.add_to_cart_button
    cart_icon = locators.cart_icon
    my_cart_text = locators.my_cart_text
    proceed_to_checkout = locators.proceed_to_checkout_button

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def search_for_product(self, product_name):
        result_flag = self.set_text(self.search_box, product_name)
        self.hit_enter(self.search_box)
        self.conditional_write(result_flag, f"Searched for product: {product_name}", "Failed to search product", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_product(self):
        scroll_flag = self.scroll_down(self.product_image)
        result_flag = False
        if scroll_flag:
            result_flag = self.click_element(self.product_image)
        self.conditional_write(result_flag, "Clicked product image", "Failed to click product image", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_size(self):
        result_flag = self.click_element(self.size_option)
        self.conditional_write(result_flag, "Selected size S", "Failed to select size S", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_color(self):
        result_flag = self.click_element(self.color_option)
        self.conditional_write(result_flag, "Selected color Green", "Failed to select color Green", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_add_to_cart(self):
        result_flag = self.click_element(self.add_to_cart_button)
        self.conditional_write(result_flag, "Clicked Add to Cart", "Failed to click Add to Cart", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def go_to_checkout(self):
        result_flag = self.click_element(self.cart_icon)
        result_flag &= self.click_element(self.proceed_to_checkout)
        self.conditional_write(result_flag, "Proceeded to checkout", "Failed to proceed to checkout", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def search_and_add_product(self, product_name="shirt"):
        result_flag = self.search_for_product(product_name)
        result_flag &= self.click_product()
        result_flag &= self.select_size()
        result_flag &= self.select_color()
        result_flag &= self.click_add_to_cart()
        result_flag &= self.go_to_checkout()

        if result_flag:
            self.switch_page("shipping page")

        self.conditional_write(result_flag,
            positive="Successfully added product and navigated to shipping page",
            negative="Failed during add to cart/checkout process",
            level='debug')
        return result_flag
