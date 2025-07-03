
'''Search object is used to search shirt'''
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Search_Object:
    search_box = locators.search_box

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def search_for_product(self, product_name):
        result_flag = self.set_text(self.search_box, product_name)
        self.hit_enter(self.search_box)
        self.conditional_write(result_flag, f"Searched for product: {product_name}", "Failed to search product", level='debug')
        return result_flag

