
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException


class ScreenDetector:
    def __init__(self, driver):
        self.driver = driver

    # Get current activity
    def get_current_activity(self) -> str:
        activity = self.driver.current_activity
        print(f"\nActivity: {activity}")
        return activity

    def is_text_present(self, text):
        elements = self.driver.find_elements(
            AppiumBy.XPATH, f'//*[@text="{text}"]'
        )
        return len(elements) > 0

    # Get toolbar title safely
    def get_toolbar_title(self) -> str:
        try:
            el = self.driver.find_element(
                AppiumBy.ID, "bn.ereader:id/toolbar_title"
            )
            raw = el.text
            clean = raw.strip().lower()
            print(f"Toolbar raw: '{raw}' | normalized: '{clean}'")
            return clean
        except NoSuchElementException:
            print("Toolbar not found")
            return ""

    # Safe element check
    def is_element_present(self, by, value) -> bool:
        try:
            self.driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False

    # MAIN DETECTOR
    def get_current_screen(self):

        try:
            activity = self.driver.current_activity

            if "MsgUMSActivity" in activity:
                return "UsbModeScreen"
            if "EpdHomeActivity" in activity:
                return "EpdHome"

            return activity

        except:
            return "DriverDead"

    def get_current_screen2(self) -> str:
        activity = self.get_current_activity()

        # =========================
        # Activity-based detection
        # =========================
        if "WelcomeIntroActivity" in activity:
            return "WelcomeIntro"

        if "ReaderActivity" in activity:
            if self.is_text_present("Our best eReader"):
                print("On correct page")
                return "Tutorial"

            print("Reader screen without tutorial")
            return "Reader"

        if "library.MainActivity" in activity:
            return "Library"

        if "search.SearchActivity" in activity:
            return "Search"

        if "AudiobookStoreActivity" in activity:
            return "Audiobooks"

        if "ORegisterUserLogin" in activity:
            return "Login"

        if "ProfileV5Activity" in activity:
            return "Account"

        if "LogoutSettingsActivity" in activity:
            return "SignOutAccount"

        if "WifiPickerActivity" in activity:
            return "WifiPicker"

        if "WebStorefrontActivity" in activity:
            title = self.get_toolbar_title()

            # robust matching
            if "ebooks" in title:
                return "Shop"

           # if "search" in title:
             #   return "Search"
            return "NONE"

        if "ProfileV5SinglePaneActivity" in activity:
            title = self.get_toolbar_title()

            # robust matching
            if "trends" in title:
               return "trends"

            if "wishlist" in title:
               return "Wishlist"

            if "favorite categories" in title:
                return "FavoriteCategories"

            if "manage profiles" in title:
               return "ManageProfiles"

            if "account" in title:
               return "AccountSettings"

            if "payment" in title:
               return "PaymentSettings"

            if "app settings" in title:
               return "AppSettings"

            if "glowlight" in title:
               return "GlowlightSettings"

            return "NONE"

        # Specific for EPD devices
        if "MsgUMSActivity" in activity:
            return "UsbModeScreen"

        if "ynt3.EpdHomeActivity" in activity:
            return "EpdHome"

        if "EpdTutorialWelcomeActivity" in activity: #first screen
            return "WelcomeToTheNewLibrary"

        if "EpdTutorialActivity" in activity:
            return "Tutorial"

        if "EpdProductDetailsActivity" in activity:
            return "EpdProductDetails"


        # =========================
        # UI fallback detection
        # =========================
        print("Falling back to UI detection...")

        if self.is_element_present(AppiumBy.ID, "bn.ereader:id/idCreateAccountEmail"):
            return "CreateAccount"

        #if self.is_element_present(AppiumBy.ID, "com.bn.nook.reader.activities.ReaderActivity"):
        #    return "Libra"

        #if self.is_element_present(AppiumBy.CLASS_NAME, "android.widget.EditText"):
          #  return "Search"

        return "Unknown"


    # Wait until screen is reached
    def wait_for_screen(self, expected_screen: str, timeout: int = 10) -> bool:
        import time

        for i in range(timeout):
            screen = self.get_current_screen()
            print(f"⏳ Attempt {i+1}: {screen}")

            if screen == expected_screen:
                print(f"Reached screen: {expected_screen}")
                return True

            time.sleep(1)

        print(f"Failed to reach screen: {expected_screen}")
        return False