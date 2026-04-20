import time


def is_ui_stable(driver):
    try:
        driver.current_activity
        driver.page_source
        return True
    except:
        return False


def wait_for_ui_stable(driver, timeout=10):
    print("⏳ Waiting for UI stability...")

    for _ in range(timeout):
        if is_ui_stable(driver):
            return True
        time.sleep(1)

    return False