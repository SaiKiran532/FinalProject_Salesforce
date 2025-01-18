import logging

from selenium.webdriver.common.by import By

from PageObjects.Locators.Locators import Locators
from GenericWrappers.WebDriverUtils import WebDriverUtils


class CreateLead(Locators):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.utils = WebDriverUtils(driver)

    def create_lead(self, salutation, first_name, last_name, company):
        """Creates a new lead."""
        try:
            # Navigate to the Sales and Leads tabs
            self.logger.info("Navigating to Sales and Leads tabs.")
            self.utils.action_click(By.XPATH, self.sales_tab)
            self.utils.wait_for_seconds(5)
            self.utils.action_click(By.XPATH, self.leads_tab)
            self.utils.wait_for_seconds(5)

            # Click the New Lead button
            self.logger.info("Clicking the New Lead button.")
            self.utils.action_click(By.CSS_SELECTOR, self.new_button)
            self.utils.wait_for_seconds(5)

            # Fill out the lead form
            self.logger.info("Filling out the lead form.")
            self.utils.click_element(By.XPATH, self.salutation)
            self.utils.click_element(By.XPATH, self.salutation_option.format(salutation))
            self.utils.send_keys(By.XPATH, self.first_name, first_name)
            self.utils.send_keys(By.XPATH, self.last_name, last_name)
            self.utils.send_keys(By.XPATH, self.company, company)

            # Save the lead
            self.logger.info("Saving the lead.")
            self.utils.click_element(By.XPATH, self.save_button)
            self.utils.wait_for_seconds(10)
            self.logger.info("Lead created successfully.")

        except Exception as e:
            self.logger.error(f"An error occurred while creating a lead: {e}")
            raise

    def verify_lead_has_created(self):
        """Verifies if the lead has been created."""
        try:
            self.logger.info("Verifying if the lead has been created.")
            element = self.utils.get_element(By.XPATH, self.verify_lead_created)
            self.logger.info("Lead verification successful.")
            return element.text

        except Exception as e:
            self.logger.error(f"An error occurred while verifying the lead: {e}")
            self.utils.take_screenshot("verify_lead_error")
            raise
