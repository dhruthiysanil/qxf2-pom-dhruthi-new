# page_objects/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 seconds timeout

    def load_login_page(self):
        """Navigate to the login page."""
        self.driver.get("https://magento.softwaretestingboard.com/customer/account/login/")

    def enter_credentials(self, email, password):
        """Enter login email and password."""
        email_field = self.wait.until(EC.visibility_of_element_located((By.ID, "email")))
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "pass")))
        email_field.send_keys(email)
        password_field.send_keys(password)

    def submit_login(self):
        """Click the Sign In button."""
        sign_in_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "send2")))
        sign_in_btn.click()

    def redirect_to_referer(self):
        """Redirect to referer page after login."""
        self.driver.get("https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS93b21lbi5odG1s/")
        # Wait for search bar to confirm page loaded
        self.wait.until(EC.visibility_of_element_located((By.ID, "search")))

    def search_for_product(self, product):
        """Search for a product using the search bar."""
        search_input = self.wait.until(EC.visibility_of_element_located((By.ID, "search")))
        search_input.send_keys(product)
        search_input.submit()
