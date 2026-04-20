from utils.driver_setup import get_driver

#Need for test cases with reboots
def restart_driver(driver):
    print("Restarting Appium session...")

    try:
        driver.quit()
    except:
        pass

    return get_driver()