from selenium.webdriver.common.by import By
from GenericWrappers.WebDriverUtils import WebDriverUtils
from PageObjects.Locators.Locators import Locators

class LoginPage(Locators):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.utils = WebDriverUtils(driver)

    def set_user_name(self, username_):
        """Set the username in the login form."""
        self.utils.clear_field(By.ID, self.username_loc_id)
        self.utils.send_keys(By.ID, self.username_loc_id, username_)

    def set_password(self, password_):
        """Set the password in the login form."""
        self.utils.clear_field(By.ID, self.password_loc_id)
        self.utils.send_keys(By.ID, self.password_loc_id, password_)

    def click_login(self):
        """Click the login button."""
        self.utils.click_element(By.ID, self.button_loc_id)
        self.utils.wait_for_seconds(10)

    def click_logout(self):
        """Perform logout operation."""
        self.utils.click_element(By.XPATH, self.profile_button)
        self.utils.wait_for_seconds(5)
        self.utils.click_element(By.LINK_TEXT, self.logout_loc_linktext)
        self.utils.wait_for_seconds(10)
