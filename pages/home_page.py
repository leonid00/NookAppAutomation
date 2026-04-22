from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.device_actions import press_back

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.LIBRARY_TAB = (AppiumBy.ACCESSIBILITY_ID, "LIBRARY")

        # Library screen indicator (NOOK logo on the left top conner in Library for now)
        self.LIBRARY_SCREEN = (AppiumBy.ID, "bn.ereader:id/toolbar_logo")

    def open_library(self):
        # If already in Library → skip click
        if self._is_library_open():
            print("Already in Library screen")
            return

        # Click Library tab

        self.wait.until(EC.element_to_be_clickable(self.LIBRARY_TAB)).click()
        #Need to find the way how to clean old data from text filed using for now back key
        activity = self.driver.current_activity
        if activity == "com.nook.lib.search.SearchActivity":
            print("Just for now work around to clear search filed")
            press_back()
        # Wait for Library screen to fully load
        self.wait.until(EC.presence_of_element_located(self.LIBRARY_SCREEN))

    # ---------- Helpers ----------

    def _is_library_open(self):
        activity = self.driver.current_activity

        print(f"Current activity: {activity}")
        try:
            self.driver.find_element(*self.LIBRARY_SCREEN)
            return True
        except:
            return False