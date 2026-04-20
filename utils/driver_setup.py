from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

def get_driver():
    options = UiAutomator2Options()
    options.automation_name = "UiAutomator2"
    options.platform_name = "Android"
    options.app_package = "bn.ereader"
    options.app_activity = ".app.ui.SplashActivity"

    options.no_reset = True
    options.new_command_timeout = 300


    # stability caps
    options.set_capability("uiautomator2ServerInstallTimeout", 60000)
    options.set_capability("adbExecTimeout", 60000)
    options.set_capability("androidInstallTimeout", 90000)
    options.set_capability("skipServerInstallation", False)

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )
    return driver