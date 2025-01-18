import logging
from selenium.webdriver.common.by import By
from PageObjects.Locators.Locators import Locators
from GenericWrappers.WebDriverUtils import WebDriverUtils


class Converts(Locators):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.utils = WebDriverUtils(driver)

    def convert_lead(self):
        """Converts a lead."""
        try:
            self.logger.info("Initiating lead conversion.")

            # Click the Convert buttons
            self.utils.wait_for_seconds(5)
            self.utils.action_click(By.XPATH, self.convert_button1)
            self.utils.wait_for_seconds(5)
            self.utils.action_click(By.XPATH, self.convert_button2)
            self.utils.wait_for_seconds(5)

            self.logger.info("Lead converted successfully.")
        except Exception as e:
            self.logger.error(f"An error occurred while converting a lead: {e}")
            self.utils.take_screenshot("convert_lead_error")
            raise

    def verify_lead_has_converted(self):
        """Verifies if the lead has been converted."""
        try:
            self.logger.info("Verifying if the lead has been converted.")
            self.utils.wait_for_seconds(5)
            element = self.utils.get_element(By.XPATH, self.lead_converted_verify)
            self.logger.info("Lead conversion verified successfully.")
            return element.text
        except Exception as e:
            self.logger.error(f"An error occurred while verifying lead conversion: {e}")
            self.utils.take_screenshot("verify_lead_error")
            raise

    def go_to_leads_page(self):
        """Navigates to the Leads page."""
        try:
            self.logger.info("Navigating to the Leads page.")
            self.utils.action_click(By.XPATH, self.goto_leads)
            self.utils.wait_for_seconds(5)
            self.logger.info("Successfully navigated to the Leads page.")
        except Exception as e:
            self.logger.error(f"An error occurred while navigating to the Leads page: {e}")
            self.utils.take_screenshot("go_to_leads_error")
            raise

    def convert_lead_using_existing_account(self, account_name):
        """Converts a lead using existing account."""
        try:
            self.logger.info("Initiating lead conversion.")

            # Click the Convert buttons
            self.utils.wait_for_seconds(5)
            self.utils.action_click(By.XPATH, self.convert_button1)
            self.utils.wait_for_seconds(5)
            self.utils.action_click(By.XPATH, self.choose_existing_account)
            self.utils.send_keys(By.XPATH, self.search_for_matching_accounts, account_name)
            self.utils.wait_for_seconds(5)
            self.utils.action_click(By.XPATH, self.select_matching_account_name.format(account_name))
            self.utils.action_click(By.XPATH, self.convert_button2)
            self.utils.wait_for_seconds(5)

            self.logger.info("Lead converted successfully.")
        except Exception as e:
            self.logger.error(f"An error occurred while converting a lead: {e}")
            self.utils.take_screenshot("convert_lead_error")
            raise
