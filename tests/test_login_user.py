# tests/test_login_and_search.py
import pytest
import os
from page_objects.PageFactory import PageFactory

def test_login_and_search_shirt(test_obj):
    """Test: Login to Magento and search for 'shirt'."""
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    if not email or not password:
        pytest.fail("EMAIL or PASSWORD not set in .env file")

    login_page = PageFactory.get_page_object("Login Page", test_obj.driver)

    login_page.load_login_page()
    login_page.enter_credentials(email, password)
    login_page.submit_login()
    login_page.redirect_to_referer()
    login_page.search_for_product("shirt")

    # ✅ Optional Assertion
    assert "shirt" in test_obj.driver.current_url.lower(), "Search for 'shirt' did not succeed."
