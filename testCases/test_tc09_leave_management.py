from configurations.config import VALID_USERNAME, VALID_PASSWORD
from pages.leavePage import LeavePage
from pages.loginPage import LoginPage
from utilities.customLogger import LogGen


class TestLeaveManagement:
    logger = LogGen.loggen()

    # Test Case - 9 : To assign leave to an employee and verify assignment

    def test_assign_leave(self, driver):
        self.logger.info("****** Test Case - 9 : Leave Management Test Started ******")
        login_page = LoginPage(driver)
        leave_page = LeavePage(driver)
        login_page.navigate_to_login_page()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        self.logger.info("****** Logged in successfully ******")
        leave_page.go_to_assign_leave()
        self.logger.info("****** Assign Leave Module Loaded Successfully ******")

        leave_page.fill_and_submit_assign_leave('Joseph', 'CAN - Personal', '2025-08-09', '2025-08-11',
                                                "Automated")

        self.logger.info("****** Assign Leave Filled ******")
        leave_page.search_in_leave_list('Joseph', '2025-08-09', '2025-08-11', 'Scheduled')
        self.logger.info("****** Test Case - 9 : Leave Management Test Completed ******")
