import logging

from selenium.webdriver.common.by import By

from PageObjects.Locators.Locators import Locators
from GenericWrappers.WebDriverUtils import WebDriverUtils


class CreateAccount(Locators):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.utils = WebDriverUtils(driver)

    def create_account(self,account_name):
        """Creates a new account."""
        try:
            # Navigate to the Account tab
            self.logger.info("Navigating to Account tab.")
            self.utils.action_click(By.XPATH, self.sales_tab)
            self.utils.wait_for_seconds(6)
            self.utils.action_click(By.XPATH, self.account_tab)
            self.utils.wait_for_seconds(5)

            # Click the New Account button
            self.logger.info("Clicking the New account button.")
            self.utils.action_click(By.CSS_SELECTOR, self.new_button)
            self.utils.wait_for_seconds(5)

            # Fill out the account form
            self.logger.info("Filling out the account form.")
            self.utils.send_keys(By.XPATH, self.account_name_box, account_name)

            # Save the lead
            self.logger.info("Saving the Account.")
            self.utils.click_element(By.XPATH, self.save_button)
            self.utils.wait_for_seconds(10)
            self.logger.info("Account created successfully.")

        except Exception as e:
            self.logger.error(f"An error occurred while creating a Account: {e}")
            raise

    def verify_account_has_created(self,account_name):
        """Verifies if the Account has been created."""
        try:
            self.logger.info("Verifying if the Account has been created.")
            element = self.utils.get_element(By.XPATH, self.verify_account_created.format(account_name))
            self.logger.info("Account verification successful.")
            return element.text

        except Exception as e:
            self.logger.error(f"An error occurred while verifying the Account: {e}")
            self.utils.take_screenshot("verify_Account_error")
            raise
