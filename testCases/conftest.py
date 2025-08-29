import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver

from configurations.config import BASE_URL
from pages.claimPage import ClaimPage
from pages.dashboardPage import DashboardPage
from pages.leavePage import LeavePage
from pages.loginPage import LoginPage


# from utilities.csv_reader import read_credentials, log_credentials_summary


# Setting default browser as Chrome in case user does not specify the browser
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on (chrome or firefox)")


# Fetching the browser and launching the application, maximize the window as setup mechanism.
@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    driver = None

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    print("\n--- Setup: Launching browser ---")
    driver.get(BASE_URL)
    driver.maximize_window()
    yield driver
    print("--- Teardown: Closing browser ---")
    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    """Return a LoginPage object bound to the test's WebDriver."""
    return LoginPage(driver)


@pytest.fixture(scope="function")
def dashboard_page(driver):
    """Return a DashboardPage object bound to the test's WebDriver."""
    return DashboardPage(driver)


@pytest.fixture(scope="function")
def claim_page(driver):
    """Return a ClaimPage object bound to the test's WebDriver."""
    return ClaimPage(driver)


@pytest.fixture(scope="function")
def leave_page(driver):
    """Return a LeavePage object bound to the test's WebDriver."""
    return LeavePage(driver)


@pytest.fixture(scope="function")
def logged_in_session(driver, login_page, dashboard_page):
    """Create logged-in session before a test, and attempt clean logout after.

    Yields:
        tuple: (driver, login_page, dashboard_page)
    """
    try:
        login_page.navigate_to_login_page()
        login_page.login("Admin", "admin123")

        # Confirm dashboard appears; swallow result as some UIs may vary
        dashboard_page.is_dashboard_loaded()

        yield driver, login_page, dashboard_page
    finally:
        try:
            dashboard_page.logout()
        except:
            # Fall back to direct navigation if logout fails (e.g., session state changes)
            driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


########## For pytest html reports #########
# hook for adding new environment info in the html report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Project 2 - HR Management Web Application'
    config.stash[metadata_key]['Module'] = 'OrangeHRM'
    config.stash[metadata_key]['Tester Name'] = 'Navin Kumar M'


# hook for delete/modify environment info in the html report
pytest.hookimpl(optionalhook=True)


def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
