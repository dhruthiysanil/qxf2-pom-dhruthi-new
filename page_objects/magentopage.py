"""
magentopage.py
Page Object class for Magento Shirt Purchase
"""
from utils.Wrapit import Wrapit
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from conf import SearchConfig

class magentopage(Wrapit):

    def __init__(self, driver):
        self.driver = driver

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def login(self, email, password):
        self.driver.get(SearchConfig.LOGIN_URL)
        self.set_text((By.ID, SearchConfig.SIGN_IN_EMAIL_INPUT), email)
        self.set_text((By.ID, SearchConfig.SIGN_IN_PASSWORD_INPUT), password)
        self.click_element((By.ID, SearchConfig.SIGN_IN_BUTTON))
        self.wait_for_element((By.ID, SearchConfig.SEARCH_INPUT_ID))
        return True

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def search_and_add_shirt(self):
        self.set_text((By.ID, SearchConfig.SEARCH_INPUT_ID), "shirt", press_enter=True)
        self.click_element((By.XPATH, SearchConfig.RADIANT_TEE_XPATH))
        self.scroll_down(500)
        self.click_element((By.ID, SearchConfig.SIZE_M_ID))
        self.click_element((By.ID, SearchConfig.COLOR_BLUE_ID))
        self.click_element((By.XPATH, SearchConfig.ADD_TO_CART_XPATH))
        return True

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def proceed_to_checkout(self):
        self.click_element((By.XPATH, SearchConfig.CART_ICON_XPATH))
        self.wait_for_element((By.CLASS_NAME, "minicart-items"))
        self.click_element((By.ID, SearchConfig.MINICART_CHECKOUT_BUTTON_ID))
        return True

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def fill_shipping_details(self):
        self.wait_for_url("checkout/#shipping")
        self.set_text(SearchConfig.CHECKOUT_COMPANY_SELECTOR, SearchConfig.COMPANY_NAME)
        self.set_text(SearchConfig.CHECKOUT_STREET_SELECTOR, SearchConfig.STREET_ADDRESS)
        self.set_text(SearchConfig.CHECKOUT_CITY_SELECTOR, SearchConfig.CITY)
        self.select_by_index(SearchConfig.CHECKOUT_STATE_DROPDOWN_SELECTOR, SearchConfig.STATE_INDEX)
        self.set_text(SearchConfig.CHECKOUT_ZIP_SELECTOR, SearchConfig.ZIP_CODE)
        self.select_by_index(SearchConfig.CHECKOUT_COUNTRY_SELECTOR, SearchConfig.COUNTRY_INDEX)
        self.set_text(SearchConfig.CHECKOUT_PHONE_SELECTOR, SearchConfig.PHONE_NUMBER)
        self.click_element(SearchConfig.SHIPPING_METHOD_RADIO_XPATH)
        self.click_element(SearchConfig.NEXT_BUTTON_XPATH)
        return True

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def place_order(self):
        self.wait_for_url("checkout/#payment")
        self.wait_for_invisibility((By.CSS_SELECTOR, "img[alt='Loading...']"))
        self.click_element(SearchConfig.PLACE_ORDER_BUTTON_XPATH)
        self.wait_for_url(SearchConfig.SUCCESS_PAGE_URL)
        return True
