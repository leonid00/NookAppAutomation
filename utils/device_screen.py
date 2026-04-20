import subprocess
import time
from utils.driver_setup import get_driver
from appium import webdriver
from appium.options.android import UiAutomator2Options

driver = get_driver()

def wake_up_screen():
    subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_WAKEUP'])
    time.sleep(1)
    print("Screen woken up")


def unlock_screen(driver):
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    print(f"📐 Screen size: {width}x{height}")
    driver.execute_script("mobile: swipeGesture", {
        "left": int(width * 0.1),
        "top": int(height * 0.9),
        "width": int(width * 0.8),
        "height": 10,
        "direction": "right",
        "percent": 1.0
    })
    print("Screen unlocked")


def swipe_bottom(driver, direction="left"):
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    print(f"📐 Screen size: {width}x{height}")
    driver.execute_script("mobile: swipeGesture", {
        "left": int(width * 0.1),
        "top": int(height * 0.9),
        "width": int(width * 0.8),
        "height": 10,
        "direction": direction,
        "percent": 1.0
    })
    print(f"Bottom swipe {direction} performed")


try:
   # is_locked = driver.is_locked()
   # driver.unlock()
   # print("Device is locked:", is_locked)

    #wake_up_screen()
    unlock_screen(driver)
    #time.sleep(1)
    #swipe_bottom(driver, direction="right")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()