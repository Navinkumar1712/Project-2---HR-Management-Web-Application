from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from configurations.config import VALID_USERNAME, VALID_PASSWORD
from pages.loginPage import LoginPage
from utilities.customLogger import LogGen


class TestLogin:
    logger = LogGen.loggen()

    # Test-Case-3 - Validate presence of login fields

    def test_presence_of_login_fields(self, driver):
        self.logger.info("****** Test Case - 3 : Validate - Presence of Login Fields Started ******")
        login_page = LoginPage(driver)
        login_page.verify_login_page_loaded()
        self.logger.info("****** Presence of Login fields validated *****")
        self.logger.info("****** Test case - 3 : Validate - Presence of Login Fields Completed ******")

    # Test Case - To verify login functionality with valid credentials.

    def test_valid_login(self, driver):
        self.logger.info("****** Test Case : Login Functionality Test Started ******")
        self.logger.info("****** Verifying Login with Valid credentials ******")
        login_page = LoginPage(driver)
        login_page.verify_login_page_loaded()
        self.logger.info("****** Login Page Loaded Successfully ******")
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        # After clicking on Login button, explicit wait of 10 seconds is used to load the elements on the DOM
        wait = WebDriverWait(driver, 10)
        elements = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//h6[normalize-space()='Dashboard']")))
        login_page.verify_successful_login()
        self.logger.info("****** Test Case : Login Functionality Test Completed ******")
