import allure
import pytest
from helpers.webdriver import BrowserManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser_type", action="store", default="firefox", help="Browser selection: 'chrome' or 'firefox'"
    )

@pytest.fixture
def driver(request):
    browser_type = request.config.getoption("--browser_type")
    web_driver = BrowserManager.create_browser(browser_type)
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()