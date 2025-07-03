"This is used to store user details"
from utils.Wrapit import Wrapit
import conf.locators_conf as locators
import time

class Shipping_Object:
    "Page object for the Shipping Page"

    # Locators from locators_conf
    CHECKOUT_COMPANY_SELECTOR = locators.CHECKOUT_COMPANY_SELECTOR
    CHECKOUT_STREET_SELECTOR = locators.CHECKOUT_STREET_SELECTOR
    CHECKOUT_CITY_SELECTOR = locators.CHECKOUT_CITY_SELECTOR
    CHECKOUT_STATE_DROPDOWN_SELECTOR = locators.CHECKOUT_STATE_DROPDOWN_SELECTOR
    CHECKOUT_ZIP_SELECTOR = locators.CHECKOUT_ZIP_SELECTOR
    CHECKOUT_COUNTRY_SELECTOR = locators.CHECKOUT_COUNTRY_SELECTOR
    CHECKOUT_PHONE_SELECTOR = locators.CHECKOUT_PHONE_SELECTOR
    BILLING_SAME_AS_SHIPPING_CHECKBOX = locators.BILLING_SAME_AS_SHIPPING_CHECKBOX
    NEXT_BUTTON_XPATH = locators.NEXT_BUTTON_XPATH
    PLACE_ORDER_BUTTON_XPATH = locators.PLACE_ORDER_BUTTON_XPATH

    @Wrapit._screenshot
    def fill_company(self, company):
        result_flag = self.set_text(self.CHECKOUT_COMPANY_SELECTOR, company)
        self.conditional_write(result_flag, "Set company name", "Failed to set company name", level='debug')
        return result_flag

    @Wrapit._screenshot
    def fill_street(self, street):
        result_flag = self.set_text(self.CHECKOUT_STREET_SELECTOR, street)
        self.conditional_write(result_flag, "Set street address", "Failed to set street address", level='debug')
        return result_flag

    @Wrapit._screenshot
    def fill_city(self, city):
        result_flag = self.set_text(self.CHECKOUT_CITY_SELECTOR, city)
        self.conditional_write(result_flag, "Set city", "Failed to set city", level='debug')
        return result_flag

    @Wrapit._screenshot
    def select_country(self, country):
        result_flag = self.select_dropdown_option(self.CHECKOUT_COUNTRY_SELECTOR, country)
        self.conditional_write(result_flag, f"Selected country: {country}", "Failed to select country", level='debug')
        self.smart_wait(self.CHECKOUT_STATE_DROPDOWN_SELECTOR, wait_seconds=10)
        return result_flag

    @Wrapit._screenshot
    def select_state(self, state):
        result_flag = self.select_dropdown_option(self.CHECKOUT_STATE_DROPDOWN_SELECTOR, state)
        self.conditional_write(result_flag, f"Selected state: {state}", "Failed to select state", level='debug')
        return result_flag

    @Wrapit._screenshot
    def fill_zip(self, zip_code):
        result_flag = self.set_text(self.CHECKOUT_ZIP_SELECTOR, zip_code)
        self.conditional_write(result_flag, "Set ZIP code", "Failed to set ZIP code", level='debug')
        return result_flag

    @Wrapit._screenshot
    def fill_phone(self, phone):
        result_flag = self.set_text(self.CHECKOUT_PHONE_SELECTOR, phone)
        self.conditional_write(result_flag, "Set phone number", "Failed to set phone number", level='debug')
        return result_flag

    @Wrapit._screenshot
    def click_next(self):
        self.smart_wait(self.NEXT_BUTTON_XPATH, wait_seconds=15)
        element = self.get_element(self.NEXT_BUTTON_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
        result_flag = self.click_element(self.NEXT_BUTTON_XPATH)
        self.conditional_write(result_flag, "Clicked Next", "Failed to click Next", level='debug')
        return result_flag

    
    @Wrapit._screenshot
    def place_order(self):
        self.smart_wait(self.PLACE_ORDER_BUTTON_XPATH, wait_seconds=15)
        result_flag = self.click_element(self.PLACE_ORDER_BUTTON_XPATH)
        self.conditional_write(result_flag, "Clicked Place Order", "Failed to click Place Order", level='debug')
        return result_flag

    @Wrapit._screenshot
    def complete_shipping_flow(self, shipping_info):
        result_flag = True
        self.smart_wait(self.NEXT_BUTTON_XPATH, wait_seconds=20)

        selected_address_div = self.driver.find_elements("css selector", "div.shipping-address-item.selected-item")
        form_filled = True if selected_address_div else False

        if not form_filled:
            self.write("No filled shipping address found. Proceeding to fill shipping form.", level="debug")
            result_flag &= self.fill_company(shipping_info["company"])
            result_flag &= self.fill_street(shipping_info["street"])
            result_flag &= self.fill_city(shipping_info["city"])
            result_flag &= self.select_country(shipping_info["country"])
            result_flag &= self.select_state(shipping_info["state_text"])
            result_flag &= self.fill_zip(shipping_info["zip"])
            result_flag &= self.fill_phone(shipping_info["phone"])
            result_flag &= self.click_next()
            result_flag &= self.place_order()
        else:
            self.write("Detected filled shipping address. Skipping form input.", level="debug")

        result_flag &= self.click_next()
        result_flag &= self.place_order()

        if result_flag:
            self.write("Your order has been placed.", level='info')

        self.conditional_write(
            result_flag,
            "Successfully completed shipping and placed the order",
            "Failed to complete shipping or place the order",
            level='debug'
        )
        return result_flag
