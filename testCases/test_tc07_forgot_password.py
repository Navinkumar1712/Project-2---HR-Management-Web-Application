import time

from selenium.webdriver.common.by import By

from configurations.config import VALID_USERNAME
from pages.loginPage import LoginPage
from utilities.customLogger import LogGen


class TestForgotPassword:
    logger = LogGen.loggen()

    # Test Case - 7: To Verify "Forgot Password" link functionality

    def test_forgot_password(self, driver):
        self.logger.info("****** Test Case - 7: Forgot Password Functionality Test Started ******")
        login_page = LoginPage(driver)
        login_page.click_forgot_password_link()
        login_page.is_forgot_password_page_loaded()
        login_page.enter_username_for_reset(VALID_USERNAME)
        login_page.submit_forgot_password_form()
        self.logger.info("****** Clicked on Reset Password Button *****")
        time.sleep(2)
        driver.find_element(By.XPATH, login_page.RESET_PASSWORD_SUCCESS_MESSAGE).is_displayed()
        self.logger.info("***** Reset Password Success Message Displayed ******")
        self.logger.info("****** Test Case - 7: Forgot Password Functionality Test Completed ******")
