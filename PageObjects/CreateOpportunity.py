import logging
from selenium.webdriver.common.by import By
from PageObjects.Locators.Locators import Locators
from GenericWrappers.WebDriverUtils import WebDriverUtils


class CreateOpportunity(Locators):
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.utils = WebDriverUtils(driver)

    def create_opportunity(self, opportunity_name,close_date, stage, forecast_category,account_name):
        """Creates a new opportunity."""
        try:
            self.logger.info("Navigating to Opportunities tab.")
            self.utils.action_click(By.XPATH, self.opportunities_tab)
            self.utils.wait_for_seconds(8)

            self.logger.info("Clicking New button to create an opportunity.")
            self.utils.action_click(By.CSS_SELECTOR, self.new_button)
            self.utils.wait_for_seconds(5)

            # Fill out the opportunity form
            self.logger.info("Filling out the opportunity form.")
            self.utils.send_keys(By.XPATH, self.opportunity_name, opportunity_name)
            self.utils.send_keys(By.XPATH, self.select_account_name, account_name)
            self.utils.wait_for_seconds(3)
            self.utils.action_click(By.XPATH, self.select_account_name)
            self.utils.action_click(By.XPATH, self.account_option.format(account_name))
            self.utils.wait_for_seconds(2)

            self.utils.send_keys(By.XPATH, self.close_date, close_date)

            # Select Stage
            self.utils.scroll_into_view(By.XPATH, self.stage)
            self.utils.action_click(By.XPATH, self.stage)
            self.utils.wait_for_seconds(3)
            self.utils.action_click(By.XPATH, self.select_stage_option.format(stage))
            self.utils.wait_for_seconds(2)

            # Select Forecast Category
            self.utils.scroll_into_view(By.XPATH, self.forecast_category)
            self.utils.action_click(By.XPATH, self.forecast_category)
            self.utils.wait_for_seconds(2)
            self.utils.action_click(By.XPATH, self.forecast_category_option.format(forecast_category))

            # Save the opportunity
            self.logger.info("Saving the opportunity.")
            self.utils.click_element(By.XPATH, self.save_button)
            self.utils.wait_for_seconds(10)

            self.logger.info("Opportunity created successfully.")
        except Exception as e:
            self.logger.error(f"An error occurred while creating an opportunity: {e}")
            self.utils.take_screenshot("create_opportunity_error")
            raise

    def verify_opportunity_has_saved(self, opportunity_name, account_name):
        """Verifies if the opportunity has been saved."""
        try:
            self.logger.info("Verifying that the opportunity has been saved.")
            self.utils.action_click(By.XPATH, self.account_tab)
            self.utils.wait_for_seconds(2)
            self.utils.action_click(By.XPATH, self.existing_account.format(account_name))
            self.utils.wait_for_seconds(2)

            element = self.utils.get_element(By.XPATH, self.verify_contact_or_opportunity.format(opportunity_name))
            self.utils.scroll_into_view(By.XPATH, self.verify_contact_or_opportunity.format(opportunity_name))
            self.logger.info("Opportunity verification successful.")
            return element.text
        except Exception as e:
            self.logger.error(f"An error occurred while verifying the opportunity: {e}")
            self.utils.take_screenshot("verify_opportunity_error")
            raise
