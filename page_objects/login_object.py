import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Login_Object:
    "Login object for Magento site"

    # Locators
    login_link = locators.sign_in_link
    email_field = locators.email_field
    password_field = locators.password_field
    sign_in_button = locators.sign_in_button
    women_section = locators.women_section
    login_success_fragment = "magento.softwaretestingboard.com"  # Or just "/" if homepage URL

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_login_link(self):
        return self.click_element(self.login_link)

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_email(self, email):
        return self.set_text(self.email_field, email)

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_password(self, password):
        return self.set_text(self.password_field, password)

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_sign_in(self):
        return self.click_element(self.sign_in_button)

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_women_section(self):
        "Click on the Women section after login"
        return self.click_element(self.women_section)

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_login_success(self):
        "Verify login success by checking the current URL"
        current_url = self.get_current_url()
        return self.login_success_fragment in current_url

    def login_to_magento(self, email, password):
        "Full login sequence including navigating to Women section"
        result_flag = False

        if self.click_login_link():
            if self.set_email(email) and self.set_password(password):
                if self.click_sign_in():
                    if self.check_login_success():
                        result_flag = self.click_women_section()

        return result_flag
