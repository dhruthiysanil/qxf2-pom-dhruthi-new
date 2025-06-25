"""
test_magento_purchase.py
Test case for Magento purchase flow using Page Object Model
"""
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.magentopage import magentopage

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def test_magento_purchase():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    try:
        page = magentopage(driver)
        assert page.login(EMAIL, PASSWORD)
        assert page.search_and_add_shirt()
        assert page.proceed_to_checkout()
        assert page.fill_shipping_details()
        assert page.place_order()
    except Exception as e:
        print("Test failed:", e)
        driver.save_screenshot("test_failure.png")
    finally:
        input("Press Enter to exit and close browser...")
        driver.quit()
