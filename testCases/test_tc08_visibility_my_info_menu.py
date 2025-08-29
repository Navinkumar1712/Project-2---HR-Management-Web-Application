from configurations.config import VALID_USERNAME, VALID_PASSWORD
from pages.dashboardPage import DashboardPage
from pages.loginPage import LoginPage
from utilities.customLogger import LogGen


class TestNavigationMyItems:
    logger = LogGen.loggen()

    # Test Case - 8: To Validate the presence of menu items under “My Info”

    def test_my_info_items_visible_clickable(self, driver):
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        self.logger.info("****** Case - 8: My Info Sub Menu Items Visibility & Clickable Test Started ******")
        login_page.verify_login_page_loaded()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        if dashboard_page.is_dashboard_loaded():
            self.logger.info("****** Dashboard Loaded Successfully ******")
            dashboard_page.click_my_info_menu()
            if dashboard_page.verify_my_info_submenu_items():
                self.logger.info("****** My Info Menu Items Visible ******")
                if dashboard_page.verify_my_info_submenu_items_clickable():
                    self.logger.info("****** My Info Menu Items Clickable ******")
                else:
                    self.logger.info("****** My Info Menu Items Not Clickable ******")
            else:
                self.logger.info("****** My Info Menu Items Not Visible ******")
        else:
            self.logger.info("****** Dashboard Not Loaded Successfully ******")
        self.logger.info("****** Case - 8: My Info Sub Menu Items Visibility & Clickable Test Completed ******")
