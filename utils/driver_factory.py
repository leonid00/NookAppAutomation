from appium import webdriver
from appium.options.android import UiAutomator2Options
from utils.devices import DEVICES

device_index = 0


def get_driver():

    global device_index

    device = DEVICES[device_index % len(DEVICES)]
    device_index += 1

    options = UiAutomator2Options()

    # ==============================
    # DEVICE CONFIG
    # ==============================
    options.udid = device["udid"]
    options.system_port = device["systemPort"]

    # ==============================
    # APP CONFIG
    # ==============================
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "bn.ereader"
    options.app_activity = ".EpdHomeActivity"
    options.no_reset = True

    # ==============================
    # OPTIONAL STABILITY FLAGS
    # ==============================
    options.new_command_timeout = 300

    return webdriver.Remote(
        command_executor="http://localhost:4723",
        options=options
    )