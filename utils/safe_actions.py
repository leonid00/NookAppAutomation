from selenium.common.exceptions import WebDriverException
from utils.ui_guard import is_ui_stable
import time


def safe_find(driver, locator, timeout=5):

    for i in range(timeout):
        try:
            if not is_ui_stable(driver):
                print("⚠️ UI unstable... retrying")
                time.sleep(1)
                continue

            return driver.find_element(*locator)

        except WebDriverException as e:
            print(f"⚠️ Retry {i+1}: {e}")
            time.sleep(1)

    raise Exception("❌ Element not found safely")