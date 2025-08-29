from selenium.webdriver.common.by import By

from configurations.config import BASE_URL
from pages.basePage import BasePage


class LoginPage(BasePage):
    # Essential locators only
    USERNAME_FIELD = (By.NAME, "username")  # Username input field
    PASSWORD_FIELD = (By.NAME, "password")  # Password input field
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")  # Login submit button
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class,'alert-content-text')]")  # Error message container
    FORGOT_PASSWORD_LINK = (
        By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")  # "Forgot your password?" link
    ORANGE_HRM_LOGO = (By.XPATH, "//div[@class='orangehrm-login-logo']//img[@alt='orangehrm-logo']")

    # Forgot password page elements
    FORGOT_PASSWORD_USERNAME_FIELD = (By.NAME, "username")
    FORGOT_PASSWORD_RESET_PASSWORD_BUTTON = (By.XPATH, "//button[normalize-space()='Reset Password']")
    FORGOT_PASSWORD_CANCEL_BUTTON = (By.XPATH, "//button[normalize-space()='Cancel']")
    FORGOT_PASSWORD_BOX_TITLE = (By.XPATH, "//h6[normalize-space()='Reset Password']")
    RESET_PASSWORD_SUCCESS_MESSAGE = "//h6[@class='oxd-text oxd-text--h6 orangehrm-forgot-password-title']"
    RESET_PASSWORD_SUCCESS_MESSAGE_1 = "//h6[normalize-space()='Reset Password link sent successfully']"

    def navigate_to_login_page(self):
        """Open the OrangeHRM login page using configured BASE_URL."""
        self.driver.get(BASE_URL)

    def login(self, username, password):
        """Perform login with provided credentials using explicit waits."""
        self.wait_for_element_visible(self.USERNAME_FIELD)
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.wait_for_element_clickable(self.LOGIN_BUTTON)
        self.click_element(self.LOGIN_BUTTON)

    def is_error_message_displayed(self):
        """Return True if error message is visible after login attempt."""
        return self.is_element_visible(self.ERROR_MESSAGE)

    def click_forgot_password_link(self):
        """Navigate to the forgot password page by clicking the link."""
        try:
            self.wait_for_element_clickable(self.FORGOT_PASSWORD_LINK)
            self.click_element(self.FORGOT_PASSWORD_LINK)
            return True
        except:
            return False

    def is_forgot_password_page_loaded(self):
        """Return True if the reset password page title is visible."""
        try:
            self.wait_for_element_visible(self.FORGOT_PASSWORD_BOX_TITLE)
            return True
        except:
            return False

    def enter_username_for_reset(self, username):
        """Type a username/email in the reset form field."""
        try:
            self.wait_for_element_visible(self.FORGOT_PASSWORD_USERNAME_FIELD)
            self.enter_text(self.FORGOT_PASSWORD_USERNAME_FIELD, username)
            return True
        except:
            return False

    def submit_forgot_password_form(self):
        """Submit the reset password form."""
        try:
            self.wait_for_element_clickable(self.FORGOT_PASSWORD_RESET_PASSWORD_BUTTON)
            self.click_element(self.FORGOT_PASSWORD_RESET_PASSWORD_BUTTON)
            return True
        except:
            return False

    def is_forgot_password_success_message_displayed(self):
        """Return True if a success/confirmation message is visible."""
        return self.is_element_visible(self.RESET_PASSWORD_SUCCESS_MESSAGE_1)

    def verify_successful_login(self):
        """Heuristic: consider login successful if URL contains 'dashboard'."""
        return "dashboard" in self.get_current_url().lower()

    def verify_failed_login(self):
        """Heuristic: consider login failed if error shown or URL contains 'login'."""
        return self.is_error_message_displayed() or "login" in self.get_current_url().lower()

    def verify_login_page_loaded(self):
        """Basic sanity check for login page fields visibility."""
        return self.is_element_visible(self.USERNAME_FIELD) and self.is_element_visible(self.PASSWORD_FIELD)
