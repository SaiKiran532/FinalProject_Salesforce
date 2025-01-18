import logging
from selenium.webdriver.common.by import By
from PageObjects.Locators.Locators import Locators
from GenericWrappers.WebDriverUtils import WebDriverUtils


class RemoveAccount(Locators):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.utils = WebDriverUtils(driver)

    def remove_account(self):
        """Removes an account by performing a series of actions."""
        try:
            self.logger.info("Navigating to Accounts tab.")
            self.utils.action_click(By.XPATH, self.account_tab)
            self.utils.wait_for_seconds(10)

            element = self.utils.get_element(By.XPATH, self.show_more)
            if element.is_displayed():
                # Click 'Show More' if the element is visible
                self.logger.info("Clicking 'Show More' to expand.")
                self.utils.action_click(By.XPATH, self.show_more)
                self.utils.wait_for_seconds(5)

                # Click 'Delete' option
                self.logger.info("Selecting 'Delete' option.")
                self.utils.action_click(By.XPATH, self.delete_option)
                self.utils.wait_for_seconds(5)

                # Confirm the deletion
                self.logger.info("Confirming delete action.")
                self.utils.action_click(By.XPATH, self.delete_button)
                self.utils.wait_for_seconds(5)

                self.logger.info("Account removed successfully.")
            else:
                self.logger.info("No account to delete.")

        except Exception as e:
            self.logger.error(f"An error occurred while removing the account: {e}")
            self.utils.take_screenshot("remove_account_error")
            raise
