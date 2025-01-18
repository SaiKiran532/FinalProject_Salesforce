import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilities.customLogger import LogGen


def before_all(context):
    """Executed once before all scenarios."""
    # Initialize logger
    context.logger = LogGen.log_gen()

    # Set up project paths
    project_root = os.path.dirname(os.path.abspath(__file__))
    screenshot_folder = os.path.join(project_root, "Screenshots")
    os.makedirs(screenshot_folder, exist_ok=True)
    context.screenshot_folder = screenshot_folder

    context.logger.info("********** Test Execution Started **********")


def before_scenario(context, scenario):
    """Executed before each scenario."""
    context.logger.info(f"Starting scenario: {scenario.name}")

    # Configure ChromeOptions to disable notifications
    chrome_options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 2}  # Disable notifications
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--start-maximized")  # Maximize the browser window

    # Initialize the WebDriver with the configured options
    context.driver = webdriver.Chrome(options=chrome_options)

    # Assign default screenshot path for the scenario
    scenario_name = scenario.name.replace(" ", "_")
    context.screenshot_path = os.path.join(context.screenshot_folder, f"{scenario_name}.png")


def after_scenario(context, scenario):
    """Executed after each scenario."""
    if scenario.status == "failed":
        # Capture a screenshot on failure
        context.driver.save_screenshot(context.screenshot_path)
        context.logger.error(f"Scenario failed: {scenario.name}")
    else:
        context.logger.info(f"Scenario passed: {scenario.name}")

    # Quit the WebDriver
    context.driver.quit()


def after_all(context):
    """Executed once after all scenarios."""
    context.logger.info("********** Test Execution Finished **********")
