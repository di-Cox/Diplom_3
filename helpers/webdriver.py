import allure
from selenium import webdriver

class BrowserManager:
    @staticmethod
    def create_browser(browser_name):
        if browser_name == "firefox":
            with allure.step('Launch Firefox browser'):
                return webdriver.Firefox()
        elif browser_name == "chrome":
            with allure.step('Launch Chrome browser'):
                return webdriver.Chrome()
        else:
            raise ValueError(f"Browser not supported: {browser_name}")