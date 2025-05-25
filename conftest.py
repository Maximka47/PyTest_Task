import allure
import pytest

from playwright.sync_api import sync_playwright

passed_tests = []
failed_tests = []

def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call":
        if result.passed:
            passed_tests.append(item.name)
        elif result.failed:
            failed_tests.append(item.name)

@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    """ Print the test summary to a file for CI/CD use (e.g., Slack notifications) """
    summary = {
        "passed": len(passed_tests),
        "failed": len(failed_tests),
        "failed_tests": failed_tests
    }

    with open("test_summary.txt", "w") as f:
        f.write(f"PASSED={summary['passed']}\n")
        f.write(f"FAILED={summary['failed']}\n")
        if summary["failed"]:
            f.write(f"FAILED_TESTS={','.join(summary['failed_tests'])}\n")

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

