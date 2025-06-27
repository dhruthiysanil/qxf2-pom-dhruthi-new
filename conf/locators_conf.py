# conf/locators_conf.py
# Common locator file for all locators


# Magento Login Page Locators
sign_in_link = "xpath,//a[normalize-space(text())='Sign In']"
email_field = "xpath,//input[@id='email']"
password_field = "xpath,//input[@id='pass']"
sign_in_button = "xpath,//button[@name='send']"  # ✅ Changed from id='send2' to name='send'
women_section = "xpath,//span[text()='Women']"
account_url_fragment = "magento.softwaretestingboard.com"
search_input = "xpath,//input[@id='search']"
radiant_tee_link = "xpath,//a[contains(@class,'product-item-link') and contains(text(),'Radiant Tee')]"

