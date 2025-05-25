import allure
import pytest

from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption("--use-browser", action="store", default="chromium", help="Browser to run tests against: chromium, firefox, webkit")

@pytest.fixture(scope="session")
def browser_name(pytestconfig):
    return pytestconfig.getoption("--use-browser")

@pytest.fixture(scope="function")
def page(browser_name):
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def capture_screenshot(page, name="screenshot"):
    screenshot = page.screenshot()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)

