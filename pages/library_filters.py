from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage

class LibraryFilters(BasePage):
    ALL_TYPES = (AppiumBy.ID, "bn.ereader:id/sliding_spinner_progress")
    BOOK = (AppiumBy.XPATH,
            '//android.widget.TextView[@resource-id="bn.ereader:id/itemtype_textview" and @text="Books"]')
    MY_FILES = (AppiumBy.XPATH,
                '//android.widget.TextView[@resource-id="bn.ereader:id/itemtype_textview" and @text="My Files"]')

    def click_books(self):
        self.wait_visible(self.BOOK).click()
        print("Books clicked")

    def click_my_files(self):
        self.wait_visible(self.MY_FILES).click()
        print("My Files clicked")
