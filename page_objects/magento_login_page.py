from selenium.webdriver.common.by import By
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class MagentoLoginPage:
    "Page object for the Magento login page (without base class)"

    # Locators
    email_field = (By.XPATH, locators.magento_email)
    password_field = (By.XPATH, locators.magento_password)
    login_button = (By.XPATH, locators.magento_login_button)
    error_message = (By.XPATH, "//div[@data-ui-id='message-error']")
    login_url = "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/"

    def __init__(self, driver):
        self.driver = driver

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def go_to(self):
        "Navigate to the login page"
        try:
            self.driver.get(self.login_url)
            result_flag = True
        except:
            result_flag = False

        self.conditional_write(result_flag,
                               positive="Navigated to login page",
                               negative="Failed to navigate to login page")
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_email(self, email):
        "Enter email into the email field"
        try:
            self.driver.find_element(*self.email_field).send_keys(email)
            result_flag = True
        except:
            result_flag = False

        self.conditional_write(result_flag,
                               positive=f"Entered email: {email}",
                               negative="Failed to enter email")
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_password(self, password):
        "Enter password into the password field"
        try:
            self.driver.find_element(*self.password_field).send_keys(password)
            result_flag = True
        except:
            result_flag = False

        self.conditional_write(result_flag,
                               positive="Entered password",
                               negative="Failed to enter password")
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def submit_login(self):
        "Click the login button"
        try:
            self.driver.find_element(*self.login_button).click()
            result_flag = True
        except:
            result_flag = False

        self.conditional_write(result_flag,
                               positive="Clicked on login button",
                               negative="Failed to click login button")
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_login_success(self):
        "Check if login was successful"
        result_flag = "customer/account" in self.driver.current_url
        self.conditional_write(result_flag,
                               positive="Login was successful",
                               negative="Login failed")
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def get_error_message(self):
        "Get login error message"
        try:
            message = self.driver.find_element(*self.error_message).text
            return message
        except:
            return None

    def conditional_write(self, result_flag, positive='', negative='', level='info'):
        "Custom logger replacement from base class"
        if result_flag:
            print(f"[{level.upper()}] {positive}")
        else:
            print(f"[{level.upper()}] {negative}")

    def write_test_summary(self):
        print("\n[SUMMARY] Test completed.\n")
