from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from configurations.config import VALID_USERNAME, VALID_PASSWORD
from pages.loginPage import LoginPage
from utilities.customLogger import LogGen


class TestLogin:
    logger = LogGen.loggen()

    # Test-Case 2 : To Verify that the home URL is accessible

    def test_valid_home_url_loading(self, driver):
        self.logger.info("****** Test Case - 2 : Verify that the Home URL is accessible - Started ******")
        login_page = LoginPage(driver)
        assert login_page.ORANGE_HRM_LOGO, "Logo not displayed, URL not loaded successfully"
        self.logger.info("****** Orange HRM Logo Displayed, URL loaded successfully ******")
        self.logger.info("****** Test Case - 2 : Verify that the Home URL is accessible - Completed ******")

   