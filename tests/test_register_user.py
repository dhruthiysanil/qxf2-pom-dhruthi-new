import pytest
import os
from page_objects.registerpage import RegisterPage  # ✅ lowercase
# from page_objects.magentoregisterpage import MagentoRegisterPage  # Not needed for this test

from page_objects.registerPage import RegisterPage


def test_register_user(test_obj):
    """Test to register a new Magento user using Qxf2 test object."""
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    if not email or not password:
        pytest.fail("EMAIL or PASSWORD not set in .env file")

    register_page = RegisterPage(test_obj.driver)
    register_page.open_homepage()
    result = register_page.fill_registration_form(email, password)

    assert result in ["success", "duplicate"], f"Unexpected registration result: {result}"
