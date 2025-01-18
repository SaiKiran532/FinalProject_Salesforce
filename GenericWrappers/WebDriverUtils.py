import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from utilities.customLogger import LogGen


class WebDriverUtils:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)
        self.logger = LogGen.log_gen()

    def click_element(self, by, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, locator))).click()
        except Exception as e:
            raise Exception(f"Failed to click element with locator {locator}: {e}")

    def send_keys(self, by, locator, value):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, locator)))
            element.clear()
            element.send_keys(value)
        except Exception as e:
            raise Exception(f"Failed to send keys to element with locator {locator}: {e}")

    def scroll_into_view(self, by, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, locator)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except Exception as e:
            raise Exception(f"Failed to scroll element with locator {locator} into view: {e}")

    def action_click(self, by, locator):
        """Performs an action chain click."""
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, locator)))
            self.action.move_to_element(element).click().perform()
        except Exception as e:
            raise Exception(f"Failed to perform action click on element with locator {locator}: {e}")

    def action_send_keys(self, by, locator, value):
        """Performs an action chain send keys."""
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, locator)))
            self.action.move_to_element(element).click().send_keys(value).perform()
        except Exception as e:
            raise Exception(f"Failed to perform action send keys on element with locator {locator}: {e}")

    def clear_field(self, by, locator):
        """Clear an input field."""
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, locator)))
            element.clear()
        except Exception as e:
            raise Exception(f"Failed to clear field with locator {locator}: {e}")

    def wait_for_seconds(self, seconds):
        """Pause the execution for a given number of seconds."""
        time.sleep(seconds)

    def get_element(self, by, locator, timeout=10):
        """Waits for an element to be present and returns it."""
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, locator)))
        except Exception as e:
            self.take_screenshot("get_element_error")
            raise

    def take_screenshot(self, name):
        """Captures a screenshot with the given name."""
        screenshot_path = f"{name}_{int(time.time())}.png"
        self.driver.save_screenshot(screenshot_path)
        self.logger.info(f"Screenshot saved: {screenshot_path}")

