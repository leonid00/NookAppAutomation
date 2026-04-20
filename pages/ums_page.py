from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.device_screen import unlock_screen
import subprocess
from utils.safe_actions import safe_find
from utils.ui_guard import is_ui_stable

import time

class UmsPage(BasePage):
    TURN_ON_BTN = (AppiumBy.ID, "com.ntx.msg:id/bn_ums_switch")
    CLOSE_BTN = (AppiumBy.ID, "com.ntx.msg:id/bn_close")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def turn_on_storage(self):
        print("turn on")
        self.tap(self.TURN_ON_BTN)

    def close_storage(self):
        print("Closing USM dialog")
        self.tap(self.CLOSE_BTN)

    def close_storage2(self):
        print("🔌 Closing USB dialog...")

        try:
            btn = safe_find(
                self.driver,
                (AppiumBy.ID, "android:id/button1")
            )
            btn.click()
            print("✅ Close clicked")

        except Exception as e:
            print(f"⚠️ Close failed: {e}")

            if is_ui_stable(self.driver):
                try:
                    self.driver.back()
                    print("🔙 Back fallback used")
                except:
                    print("❌ Back failed")
            else:
                print("⚠️ Skipping back (UI unstable)")

    def wait_for_ums_screen(self, timeout=15):
        print("⏳ Waiting for USB mode screen...")

        for i in range(timeout):
            try:
                activity = self.driver.current_activity
                print(f"Attempt {i+1}: {activity}")

                if "MsgUMSActivity" in activity:
                    print("✅ USB screen detected")
                    return True

            except Exception as e:
                print(f"⚠️ Driver issue: {e}")
                return False

            time.sleep(1)

        return False


