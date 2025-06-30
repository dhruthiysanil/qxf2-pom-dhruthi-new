'''Shipping Object which will enter all shipping details'''
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Shipping_Object:
    # "Shipping object for Magento checkout page"

    # Locators from conf
    company_field = locators.CHECKOUT_COMPANY_SELECTOR
    street_field = locators.CHECKOUT_STREET_SELECTOR
    city_field = locators.CHECKOUT_CITY_SELECTOR
    state_dropdown = locators.CHECKOUT_STATE_DROPDOWN_SELECTOR
    zip_field = locators.CHECKOUT_ZIP_SELECTOR
    country_dropdown = locators.CHECKOUT_COUNTRY_SELECTOR
    phone_field = locators.CHECKOUT_PHONE_SELECTOR

    shipping_method_radio = locators.SHIPPING_METHOD_RADIO_XPATH
    next_button = locators.NEXT_BUTTON_XPATH
    place_order_button = locators.PLACE_ORDER_BUTTON_XPATH

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def fill_shipping_form(self):
        # "Fill all shipping address fields using dropdown selection for State and Country"
        result_flag = True

        result_flag &= self.set_text(self.company_field, locators.COMPANY_NAME)
        result_flag &= self.set_text(self.street_field, locators.STREET_ADDRESS)
        result_flag &= self.set_text(self.city_field, locators.CITY)

        # Select first non-empty state option
        first_state_option = self.get_first_dropdown_value(self.state_dropdown)
        result_flag &= self.select_dropdown_option(self.state_dropdown, first_state_option)

        result_flag &= self.set_text(self.zip_field, locators.ZIP_CODE)

        # Select first non-empty country option
        first_country_option = self.get_first_dropdown_value(self.country_dropdown)
        result_flag &= self.select_dropdown_option(self.country_dropdown, first_country_option)

        result_flag &= self.set_text(self.phone_field, locators.PHONE_NUMBER)

        self.conditional_write(result_flag,
            positive="Shipping form filled successfully",
            negative="Failed to fill shipping form",
            level='debug')
        return result_flag

    def get_first_dropdown_value(self, locator):
        # extract the first dropdown value without using By"
        try:
            dropdown = self.get_element(locator)
            options = dropdown.find_elements("tag name", "option")  # No By needed
            for option in options:
                value = option.get_attribute("value")
                if value:  # Skip empty
                    return option.text
        except Exception as e:
            self.write(f"Error extracting first dropdown option: {str(e)}", "critical")
        return None

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_shipping_method(self):
        # "Select flat rate shipping option"
        result_flag = self.click_element(self.shipping_method_radio)
        self.conditional_write(result_flag,
            positive="Selected flat rate shipping method",
            negative="Failed to select shipping method",
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_next(self):
        # "Click on Next button to proceed to payment"
        result_flag = self.click_element(self.next_button)
        self.conditional_write(result_flag,
            positive="Clicked on Next button",
            negative="Failed to click Next button",
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def place_order(self):
        # "Click on Place Order button"
        result_flag = self.click_element(self.place_order_button)
        self.conditional_write(result_flag,
            positive="Clicked on Place Order",
            negative="Failed to click Place Order",
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def complete_shipping_flow(self):
        # "Full shipping form and proceed to place order"
        result_flag = self.fill_shipping_form()
        result_flag &= self.select_shipping_method()
        result_flag &= self.click_next()
        self.wait(5)  # Wait for Place Order button to load
        result_flag &= self.place_order()

        self.conditional_write(result_flag,
            positive="Completed shipping and placed order",
            negative="Failed during shipping or placing order",
            level='debug')
        return result_flag
