from pages.loginPage import LoginPage
from utilities import excel_utils
from utilities.customLogger import LogGen


class TestLoginDataDriven:
    path = ".//testdata/login_testdata.xlsx"
    logger = LogGen.loggen()

    # Test Case - 1 - To Verify Data Driven Login Functionality test with Valid and Invalid credentials from an Excel file.

    def test_login_data_driven(self, driver):
        self.logger.info("****** Test Case 1 : Verifying Login - Data Driven Login Started ******")
        login_page = LoginPage(driver)
        login_page.verify_login_page_loaded()
        self.logger.info("****** Login Page Loaded Successfully ******")

        self.rows = excel_utils.getRowCount(self.path, 'Sheet1')
        print("Number of rows", self.rows)

        for r in range(2, self.rows + 1):
            self.username = excel_utils.readData(self.path, 'Sheet1', r, 1)
            self.password = excel_utils.readData(self.path, 'Sheet1', r, 2)
            self.exp_login = excel_utils.readData(self.path, 'Sheet1', r, 3)

            login_page.login(self.username, self.password)

            if "dashboard" in driver.current_url:
                self.logger.info("****** Test Login Successful ******")
                from pages.dashboardPage import DashboardPage
                dashboard_page = DashboardPage(driver)
                dashboard_page.logout()
                self.logger.info("****** Logging Out For Valid User ******")

            elif login_page.ERROR_MESSAGE:
                self.logger.info("****** Error Message Displayed for Invalid Login Credentials ******")
        self.logger.info("****** Test Case 1 : Verifying Login - Data Driven Login Completed ******")
