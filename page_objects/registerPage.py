# page_objects/RegisterPage.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium.webdriver.common.by import By
from conf import WomenConfig


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def open_homepage(self):
        """Navigazte to the homepage."""
        self.driver.get(WomenConfig.HOME_URL)

    def fill_registration_form(self, email, password):
        """Fill out the registration form."""
        self.driver.find_element(By.XPATH, WomenConfig.CREATE_ACCOUNT_LINK).click()
        self.driver.find_element(By.ID, WomenConfig.FIRST_NAME_INPUT).send_keys("Dhruthi")
        self.driver.find_element(By.ID, WomenConfig.LAST_NAME_INPUT).send_keys("Sanil")
        self.driver.find_element(By.ID, WomenConfig.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(By.ID, WomenConfig.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(By.ID, WomenConfig.CONFIRM_PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(By.XPATH, WomenConfig.CREATE_ACCOUNT_BUTTON).click()

        try:
            error = self.driver.find_element(By.CLASS_NAME, "message-error")
            print("Registration failed: Email already exists.")
            return "duplicate"
        except:
            print("Account created successfully.")
            return "success"
