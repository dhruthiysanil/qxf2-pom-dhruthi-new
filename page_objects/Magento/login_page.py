import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf import SearchConfig
from selenium.webdriver.common.by import By
from utils.Wrapit import Wrapit

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.screenshot_counter = 1
        self.current_console_log_errors = []

    def save_screenshot(self, name):
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        self.driver.save_screenshot(f"screenshots/{name}.png")

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def load_login_page(self):
        self.driver.get(SearchConfig.LOGIN_URL)
        return "login" in self.driver.current_url

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def enter_credentials(self, email, password):
        self.wait.until(EC.visibility_of_element_located(SearchConfig.SIGN_IN_EMAIL_INPUT)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(SearchConfig.SIGN_IN_PASSWORD_INPUT)).send_keys(password)
        return True

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def submit_login(self):
        self.wait.until(EC.element_to_be_clickable(SearchConfig.SIGN_IN_BUTTON)).click()
        return True

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def redirect_to_women_page(self):
        self.driver.get(f"{SearchConfig.HOME_URL}women.html")
        return self.wait.until(EC.visibility_of_element_located(SearchConfig.SEARCH_BAR)) is not None

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def search_for_product(self, product):
        search_input = self.wait.until(EC.visibility_of_element_located(SearchConfig.SEARCH_BAR))
        search_input.clear()
        search_input.send_keys(product)
        search_input.submit()
        return True

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_radiant_tee(self):
        self.driver.get(f"{SearchConfig.HOME_URL}radiant-tee.html")
        return "radiant-tee" in self.driver.current_url