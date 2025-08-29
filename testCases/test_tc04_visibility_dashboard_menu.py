from configurations.config import VALID_USERNAME, VALID_PASSWORD
from pages.dashboardPage import DashboardPage
from pages.loginPage import LoginPage
from utilities.customLogger import LogGen


class TestNavigation:
    logger = LogGen.loggen()

    # Test Case 4 - To Verify visibility and clickable of main menu items after login

    def test_main_menu_items_visible_clickable(self, driver):
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        self.logger.info("****** Main Menu Items Visibility & Clickable Test Started ******")
        login_page.verify_login_page_loaded()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        if dashboard_page.is_dashboard_loaded():
            self.logger.info("****** Dashboard Loaded Successfully ******")
            if dashboard_page.verify_menu_items_visibility():
                self.logger.info("****** Main Menu Items Visible ******")
                if dashboard_page.verify_menu_items_clickable():
                    self.logger.info("****** Main Menu Items Clickable ******")
                else:
                    self.logger.info("****** Main Menu Items Not Clickable ******")
            else:
                self.logger.info("****** Main Menu Items Not Visible *****")
        else:
            self.logger.info("****** Dashboard Not Loaded Successfully ******")
        self.logger.info("****** Main Menu Items Visibility & Clickable Test Completed ******")
