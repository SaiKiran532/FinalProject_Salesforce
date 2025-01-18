import logging
from PageObjects.Locators.Locators import Locators
from selenium.webdriver.common.by import By
from GenericWrappers.WebDriverUtils import WebDriverUtils


class CreateContact(Locators):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.utils = WebDriverUtils(driver)

    def create_contact(self, salutation, first_name, last_name, account_name):
        """Creates a new contact."""
        try:
            # Navigate to the Contacts tab and click 'New'
            self.logger.info("Navigating to the Contact tab and creating a new contact.")
            self.utils.action_click(By.XPATH, self.contact_tab)
            self.utils.wait_for_seconds(8)
            self.utils.action_click(By.CSS_SELECTOR, self.new_button)
            self.utils.wait_for_seconds(5)

            # Fill out the contact form
            self.logger.info("Filling out the contact form.")
            self.utils.action_click(By.XPATH, self.salutation)
            self.utils.wait_for_seconds(5)
            self.utils.click_element(By.XPATH, self.salutation_option.format(salutation))
            self.utils.send_keys(By.XPATH, self.contact_first_name, first_name)
            self.utils.send_keys(By.XPATH, self.contact_last_name, last_name)
            self.utils.send_keys(By.XPATH, self.select_account_name, account_name)
            self.utils.wait_for_seconds(2)
            self.utils.click_element(By.XPATH, self.select_account_name)
            self.utils.wait_for_seconds(2)
            self.utils.action_click(By.XPATH, self.account_option.format(account_name))
            self.utils.wait_for_seconds(5)

            # Save the contact
            self.logger.info("Saving the contact.")
            self.utils.click_element(By.XPATH, self.save_button)
            self.utils.wait_for_seconds(10)
            self.logger.info("Contact saved successfully.")

        except Exception as e:
            self.logger.error(f"An error occurred while creating a contact: {e}")
            self.utils.take_screenshot("create_contact_error")
            raise

    def verify_contact_has_saved(self, contact_name, account_name):
        """Verifies if the contact has been saved under the specified account."""
        try:
            self.logger.info(f"Verifying if the contact '{contact_name}' is saved under account '{account_name}'.")
            self.utils.action_click(By.XPATH, self.account_tab)
            self.utils.wait_for_seconds(2)
            self.utils.action_click(By.XPATH, self.existing_account.format(account_name))
            self.utils.wait_for_seconds(2)

            # Verifying contact
            element = self.utils.get_element(By.XPATH, self.verify_contact_or_opportunity.format(contact_name))
            self.logger.info(f"Contact '{contact_name}' found successfully.")
            return element.text

        except Exception as e:
            self.logger.error(f"An error occurred while verifying the contact: {e}")
            self.utils.take_screenshot("verify_contact_error")
            raise
