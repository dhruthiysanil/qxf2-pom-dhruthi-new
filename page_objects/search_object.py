import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Search_Object:
    "Handles product search on Magento"

    search_input = locators.search_input  # Locator for search bar
    radiant_tee = locators.radiant_tee_link  # Locator for Radiant Tee link

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def search_for(self, product_name="shirt"):
        "Search for a product, click on the result, then close the window"
        result_flag = True

        # Type the product name into the search bar
        result_flag &= self.set_text(self.search_input, product_name)

        # Press Enter to trigger the search
        result_flag &= self.press_enter_key(self.search_input)

        # Wait for results to load
        self.wait(3)

        # Click the product link (e.g., Radiant Tee)
        result_flag &= self.click_element(self.radiant_tee)

        # Optional: Close the current tab after clicking the product
        result_flag &= self.close_current_window()

        return result_flag
