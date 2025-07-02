"This is used to store user details"
from utils.Wrapit import Wrapit
import conf.locators_conf as locators

class Shipping_Object:
    "Page object for the Shipping Page"

    # Constants from locators_conf
    COMPANY_NAME = locators.COMPANY_NAME
    STREET_ADDRESS = locators.STREET_ADDRESS
    CITY = locators.CITY
    ZIP_CODE = locators.ZIP_CODE
    COUNTRY_TEXT = locators.COUNTRY_TEXT
    PHONE_NUMBER = locators.PHONE_NUMBER

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

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def fill_company(self):
        result_flag = self.set_text(self.CHECKOUT_COMPANY_SELECTOR, self.COMPANY_NAME)
        self.conditional_write(result_flag, "Set company name", "Failed to set company name", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def fill_street(self):
        result_flag = self.set_text(self.CHECKOUT_STREET_SELECTOR, self.STREET_ADDRESS)
        self.conditional_write(result_flag, "Set street address", "Failed to set street address", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def fill_city(self):
        result_flag = self.set_text(self.CHECKOUT_CITY_SELECTOR, self.CITY)
        self.conditional_write(result_flag, "Set city", "Failed to set city", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_country(self):
        result_flag = self.select_dropdown_option(self.CHECKOUT_COUNTRY_SELECTOR, self.COUNTRY_TEXT)
        self.conditional_write(result_flag, "Selected country", "Failed to select country", level='debug')
        self.smart_wait(self.CHECKOUT_STATE_DROPDOWN_SELECTOR, wait_seconds=10)
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_state(self):
        result_flag = False
        try:
            dropdown = self.get_element(self.CHECKOUT_STATE_DROPDOWN_SELECTOR)
            if dropdown:
                options = dropdown.find_elements("tag name", "option")
                if options and len(options) >= 5:
                    options[4].click()
                    selected_text = options[4].text
                    self.write(f"Selected 5th state: {selected_text}", level='debug')
                    result_flag = True
        except Exception as e:
            self.write(str(e), 'critical')
            self.exceptions.append("Failed to select state from dropdown")
        self.conditional_write(result_flag, "Selected 5th state", "Failed to select 5th state", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def fill_zip(self):
        result_flag = self.set_text(self.CHECKOUT_ZIP_SELECTOR, self.ZIP_CODE)
        self.conditional_write(result_flag, "Set ZIP code", "Failed to set ZIP code", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def fill_phone(self):
        result_flag = self.set_text(self.CHECKOUT_PHONE_SELECTOR, self.PHONE_NUMBER)
        self.conditional_write(result_flag, "Set phone number", "Failed to set phone number", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_next(self):
        result_flag = False
        try:
            self.smart_wait(self.NEXT_BUTTON_XPATH, wait_seconds=10)
            element = self.get_element(self.NEXT_BUTTON_XPATH)
            if element:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                result_flag = self.click_element(self.NEXT_BUTTON_XPATH)
                result_flag = True
        except Exception as e:
            self.write(f"Exception in clicking Next: {str(e)}", level='critical')
            self.exceptions.append("Failed to click Next button")
        self.conditional_write(result_flag, "Clicked Next", "Failed to click Next", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_billing_checkbox_if_unchecked(self):
        result_flag = False
        try:
            self.smart_wait(self.BILLING_SAME_AS_SHIPPING_CHECKBOX, wait_seconds=10)
            checkbox = self.get_element(self.BILLING_SAME_AS_SHIPPING_CHECKBOX)
            if checkbox and not checkbox.is_selected():
                self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
                checkbox.click()
                self.write("Checked 'billing same as shipping' checkbox", level='debug')
            else:
                self.write("'billing same as shipping' checkbox already selected", level='debug')
            result_flag = True
        except Exception as e:
            self.write(f"Exception in checking billing checkbox: {str(e)}", level='critical')
            self.exceptions.append("Failed to check billing checkbox")
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def place_order(self):
        self.click_billing_checkbox_if_unchecked()
        result_flag = self.click_element(self.PLACE_ORDER_BUTTON_XPATH)
        self.conditional_write(result_flag, "Clicked Place Order", "Failed to click Place Order", level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def complete_shipping_flow(self):
        "Perform full shipping form or skip to placing order if already filled"
        result_flag = True

        try:
            self.smart_wait(self.NEXT_BUTTON_XPATH, wait_seconds=20)

            form_filled = False

            try:
                selected_address_div = self.driver.find_elements(
                    "css selector", "div.shipping-address-item.selected-item"
                )
                if selected_address_div:
                    self.write("Detected filled shipping address. Skipping form input.", level="debug")
                    form_filled = True
                else:
                    self.write("No filled shipping address found. Proceeding to fill shipping form.", level="debug")
            except Exception as e:
                self.write(f"Error while checking for filled address block: {str(e)}", level='debug')

            if not form_filled:
                result_flag &= self.fill_company()
                result_flag &= self.fill_street()
                result_flag &= self.fill_city()
                result_flag &= self.select_country()
                result_flag &= self.select_state()
                result_flag &= self.fill_zip()
                result_flag &= self.fill_phone()
            else:
                self.write("Shipping form skipped as it's already filled.", level="debug")

            result_flag &= self.click_next()
            result_flag &= self.place_order()

            if result_flag:
                self.write(" Your order has been placed.", level='info')

            self.conditional_write(
                result_flag,
                "Successfully completed shipping and placed the order",
                "Failed to complete shipping or place the order",
                level='debug'
            )

        except Exception as e:
            self.write(f"Exception in complete_shipping_flow: {str(e)}", level='critical')
            self.exceptions.append("Shipping flow error")
            result_flag = False

        return result_flag
