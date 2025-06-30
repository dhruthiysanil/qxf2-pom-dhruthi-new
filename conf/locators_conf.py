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

# Search input field
search_box = 'id,search'

# Product image (Circe Hooded Ice Fleece)
product_circe_image = "xpath,//a[contains(@class,'product-item-link') and normalize-space(text())='Circe Hooded Ice Fleece']"

# Size: S
size_s = "id,option-label-size-143-item-167"

# Color: Green
color_green = "id,option-label-color-93-item-53"

# Add to Cart
add_to_cart_button = "xpath,//button[@title='Add to Cart']"

# Cart related
cart_icon = "xpath,//a[@class='action showcart']"
my_cart_text = "xpath,//span[text()='My Cart']"
proceed_to_checkout_button = "id,top-cart-btn-checkout"

# -----------------------------
# ✅ Shipping Page Locators
# -----------------------------

CHECKOUT_COMPANY_SELECTOR = "name,company"
CHECKOUT_STREET_SELECTOR = "name,street[0]"
CHECKOUT_CITY_SELECTOR = "name,city"
CHECKOUT_STATE_DROPDOWN_SELECTOR = "name,region_id"
CHECKOUT_ZIP_SELECTOR = "name,postcode"
CHECKOUT_COUNTRY_SELECTOR = "name,country_id"
CHECKOUT_PHONE_SELECTOR = "name,telephone"

# Shipping Method and Final Checkout
SHIPPING_METHOD_RADIO_XPATH = "xpath,//input[@type='radio' and contains(@value,'flatrate')]"
NEXT_BUTTON_XPATH = "xpath,//span[@data-bind=\"i18n: 'Next'\"]"
PLACE_ORDER_BUTTON_XPATH = "xpath,//span[@data-bind=\"i18n: 'Place Order'\"]"

# -----------------------------
# ✅ Shipping Info Constants
# -----------------------------

COMPANY_NAME = "NethraTech Pvt Ltd"
STREET_ADDRESS = "123 AI Street"
CITY = "Bangalore"
STATE_INDEX = 1               # 1st index in dropdown (0-based)
ZIP_CODE = "560001"
COUNTRY_INDEX = 1             # 1st index in dropdown
PHONE_NUMBER = "9844543210"
