from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition)

    def tap(self, locator):
        for i in range(3):
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except Exception as e:
                print(f"")
                print(e)

    def tap_if_present(self, locator):
        elements = self.driver.find_elements(*locator)
        if elements:
            elements[0].click()

    def type(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        # element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    def get_current_screen(self) -> str:
        screens = {
            "Library": [
                (AppiumBy.ID, "bn.ereader:id/action_search"),
            ],
            "Login": [
                (AppiumBy.ID, "bn.ereader:id/email"),
            ],
            "Reader": [
                (AppiumBy.ID, "bn.ereader:id/reader_view"),
            ],
            "Search": [
                (AppiumBy.CLASS_NAME, "android.widget.EditText"),
            ],
        }

        for screen, locators in screens.items():
            for locator in locators:
                if self.finds(locator):
                    return screen

        return "Unknown"