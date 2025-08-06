# """
# Get the webrivers for local browsers.
# """
# from selenium.webdriver.chrome.options import Options
# import sys
# from selenium import webdriver

# class LocalOptions():
#     """Class contains methods for getting webfrivers for various browsers."""

#     @staticmethod
#     def firefox_local(browser_version):
#         """Get webdriver for firefox."""
#         options = webdriver.FirefoxOptions()
#         options.browser_version = browser_version
#         local_driver = webdriver.Firefox(options=options)

#         return local_driver

#     @staticmethod
#     def edge_local(browser_version):
#         """Get webdriver for Edge."""
#         options = webdriver.EdgeOptions()
#         options.browser_version = browser_version
#         local_driver = webdriver.Edge(options=options)

#         return local_driver

#     @staticmethod
#     def chrome_local(browser_version):
#         """Get webdriver for chrome."""
#         options = webdriver.ChromeOptions()
#         options.browser_version = browser_version
#         local_driver = webdriver.Chrome(options=options)

#         return local_driver

#     @staticmethod
#     def safari_local():
#         """Get webdriver for safari."""
#         local_driver = webdriver.Safari()

#         return local_driver

#     @staticmethod
#     def headless_chrome(browser_version):
#         """Set up headless chrome driver options and get webdriver for headless chrome."""
#         options = Options()
#         options.headless = True
#         options.browser_version = browser_version
#         options.add_argument("--window-size=1920,1080")
#         options.add_argument("--disable-extensions")
#         options.add_argument("--proxy-server='direct://'")
#         options.add_argument("--proxy-bypass-list=*")
#         options.add_argument("--start-maximized")
#         options.add_argument('--headless')
#         options.add_argument('--disable-gpu')
#         options.add_argument('--disable-dev-shm-usage')
#         options.add_argument('--no-sandbox')
#         options.add_argument('--ignore-certificate-errors')
#         local_driver = webdriver.Chrome(options=options)

#         return local_driver

#     def app_details(self, desired_capabilities, app_package, app_activity):
#         desired_capabilities['appPackage'] = app_package
#         desired_capabilities['appActivity'] = app_activity
#         return desired_capabilities

#     def app_name(self, desired_capabilities, app_path, app_name):
#         import os
#         desired_capabilities['app'] = os.path.join(app_path, app_name)
#         return desired_capabilities

#     def ios_capabilities(self, desired_capabilities, app_package, no_reset_flag, ud_id, org_id, signing_id):
#         desired_capabilities['bundleId'] = app_package
#         desired_capabilities['noReset'] = no_reset_flag
#         if ud_id is not None:
#             desired_capabilities['udid'] = ud_id
#             desired_capabilities['xcodeOrgId'] = org_id
#             desired_capabilities['xcodeSigningId'] = signing_id
#         return desired_capabilities

#     def set_mobile_device(self, mobile_os_name, mobile_os_version, device_name, orientation):
#         """Setup the mobile device."""
#         desired_capabilities = {}
#         desired_capabilities['platformName'] = mobile_os_name
#         desired_capabilities['platformVersion'] = mobile_os_version
#         desired_capabilities['deviceName'] = device_name
#         desired_capabilities['orientation'] = orientation

#         return desired_capabilities
"""
Get the webdrivers for local browsers.
"""
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class LocalOptions:
    """Class contains methods for getting webdrivers for various browsers."""

    @staticmethod
    def chrome_local(browser_version=None):
        """Get webdriver for Chrome."""
        options = webdriver.ChromeOptions()
        if browser_version:
            options.browser_version = browser_version
        return webdriver.Chrome(options=options)

    @staticmethod
    def firefox_local(browser_version=None):
        """Get webdriver for Firefox."""
        options = webdriver.FirefoxOptions()
        if browser_version:
            options.browser_version = browser_version
        return webdriver.Firefox(options=options)

    @staticmethod
    def edge_local(browser_version=None):
        """Get webdriver for Edge."""
        options = webdriver.EdgeOptions()
        if browser_version:
            options.browser_version = browser_version
        return webdriver.Edge(options=options)

    @staticmethod
    def safari_local():
        """Get webdriver for Safari."""
        return webdriver.Safari()

    @staticmethod
    def headless_chrome(browser_version=None):
        """Set up headless Chrome driver options."""
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-certificate-errors')
        if browser_version:
            options.browser_version = browser_version
        return webdriver.Chrome(options=options)

    def app_details(self, desired_capabilities, app_package, app_activity):
        """Add Android app details."""
        desired_capabilities['appPackage'] = app_package
        desired_capabilities['appActivity'] = app_activity
        return desired_capabilities

    def app_name(self, desired_capabilities, app_path, app_name):
        """Add full app path."""
        desired_capabilities['app'] = os.path.join(app_path, app_name)
        return desired_capabilities

    def ios_capabilities(self, desired_capabilities, app_package, no_reset_flag, ud_id=None, org_id=None, signing_id=None):
        """Set iOS capabilities."""
        desired_capabilities['bundleId'] = app_package
        desired_capabilities['noReset'] = no_reset_flag
        if ud_id:
            desired_capabilities['udid'] = ud_id
            desired_capabilities['xcodeOrgId'] = org_id
            desired_capabilities['xcodeSigningId'] = signing_id
        return desired_capabilities

    def set_mobile_device(self, mobile_os_name, mobile_os_version, device_name, orientation):
        """Setup the mobile device."""
        return {
            'platformName': mobile_os_name,
            'platformVersion': mobile_os_version,
            'deviceName': device_name,
            'orientation': orientation
        }
