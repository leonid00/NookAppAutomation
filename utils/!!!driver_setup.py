from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_driver(options):
    return webdriver.Remote(
        command_executor="http://localhost:4723",
        options=options
    )