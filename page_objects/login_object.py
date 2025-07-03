"""
Login Object which will redirect to Women Section and then switch to Landing_Page
"""
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
    login_success_fragment = locators.link
    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_login_link(self):
        result_flag = self.click_element(self.login_link)
        self.conditional_write(result_flag,
            positive='Clicked on login link',
            negative='Failed to click login link',
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_email(self, email):
        result_flag = self.set_text(self.email_field, email)
        self.conditional_write(result_flag,
            positive=f'Set the email to: {email}',
            negative='Failed to set email',
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_password(self, password):
        result_flag = self.set_text(self.password_field, password)
        self.conditional_write(result_flag,
            positive='Set the password',
            negative='Failed to set password',
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_sign_in(self):
        result_flag = self.click_element(self.sign_in_button)
        self.conditional_write(result_flag,
            positive='Clicked on sign in button',
            negative='Failed to click sign in button',
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_login_success(self):
        result_flag = False
        current_url = self.get_current_url()
        if self.login_success_fragment in current_url:
            result_flag = True
            self.switch_page("landing page")
        self.conditional_write(result_flag,
            positive='Login successful',
            negative='Login may have failed',
            level='debug')
        
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def login_to_magento(self, email, password):
        "Full login sequence including navigating to Women section and switching to landing page"
        result_flag = self.click_login_link()
        result_flag &= self.set_email(email)
        result_flag &= self.set_password(password)
        result_flag &= self.click_sign_in()
        result_flag &= self.check_login_success()
        self.conditional_write(result_flag,
            positive='Successfully logged in and navigated to Women section',
            negative='Failed during Magento login flow',
            level='debug')

        return result_flag
