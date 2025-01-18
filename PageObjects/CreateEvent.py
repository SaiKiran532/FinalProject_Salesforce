import logging

from selenium.webdriver.common.by import By

from PageObjects.Locators.Locators import Locators
from GenericWrappers.WebDriverUtils import WebDriverUtils


class CreateEvent(Locators):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.utils = WebDriverUtils(driver)

    def create_event(self, subject):
        """Creates a new event."""
        try:
            # Navigate to the Sales and calendar tabs
            self.logger.info("Navigating to Sales and calendar tabs.")
            self.utils.action_click(By.XPATH, self.sales_tab)
            self.utils.wait_for_seconds(5)
            self.utils.action_click(By.XPATH, self.calender_tab)
            self.utils.wait_for_seconds(10)

            # Click the New event button
            self.logger.info("Clicking the New event button.")
            self.utils.action_click(By.XPATH, self.new_event)
            self.utils.wait_for_seconds(5)

            # Fill out the event form
            self.logger.info("Filling out the event form.")
            self.utils.send_keys(By.XPATH, self.subject, subject)

            # Save the event
            self.logger.info("Saving the event.")
            self.utils.click_element(By.XPATH, self.save_event)
            self.utils.wait_for_seconds(10)
            self.logger.info("event created successfully.")

        except Exception as e:
            self.logger.error(f"An error occurred while creating a event: {e}")
            raise

    def verify_event_has_added(self,event_name):
        """Verifies if the event has been added."""
        try:
            self.logger.info("Verifying if the event has been added.")
            self.utils.scroll_into_view(By.XPATH,self.event_verification.format(event_name))
            element = self.utils.get_element(By.XPATH, self.event_verification.format(event_name))
            self.logger.info("event verification successful.")
            return element.text

        except Exception as e:
            self.logger.error(f"An error occurred while verifying the added: {e}")
            self.utils.take_screenshot("verify_event_added_error")
            raise
