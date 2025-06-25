# utils/WebDriver_Wrapper.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

class WebDriver_Wrapper:
    def __init__(self):
        self.driver = self.get_chrome_driver()

    def get_chrome_driver(self):
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        return driver

    def open_url(self, url):
        self.driver.get(url)
        return True

    def close_browser(self):
        self.driver.quit()
