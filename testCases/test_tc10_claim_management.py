import time

from configurations.config import VALID_USERNAME, VALID_PASSWORD
from pages.basePage import BasePage
from pages.claimPage import ClaimPage
from pages.dashboardPage import DashboardPage
from pages.loginPage import LoginPage
from utilities.customLogger import LogGen


class TestClaimManagement:
    logger = LogGen.loggen()

    def test_initiate_claim_request(self, driver):
        login_page = LoginPage(driver)
        base_page = BasePage(driver)
        dashboard_page = DashboardPage(driver)
        claim_page = ClaimPage(driver)
        login_page.navigate_to_login_page()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)  # OrangeHRM demo admin creds
        if dashboard_page.is_dashboard_loaded():
            driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/claim/submitClaim")
            claim_page.is_claim_page_loaded()
            self.logger.info("Submit Claim Page Loaded")
            claim_page.fill_claim_form("Travel", "USD", claim_page.enter_remarks())
            time.sleep(10)
            driver.save_screenshot(".\\screenshots\\" + "claim.png")
            self.logger.info("Claim Submitted Successfully")
        else:
            self.logger.info("Dashboard Page not displayed")
        self.logger.info("Submit Claim Test Completed")
