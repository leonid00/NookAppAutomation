import time

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LibraryPage(BasePage):

    SEARCH_BUTTON = (AppiumBy.ID, "bn.ereader:id/action_search")
    SEARCH_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    BOOK = (AppiumBy.ID, "bn.ereader:id/cover_border")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_search(self):
        self.find(self.SEARCH_BUTTON).click()

    def search_book(self, name):
        self.open_search()
        self.find(self.SEARCH_INPUT).send_keys(name)
        time.sleep(2)


    def is_book_present(self, name):
        elements = self.finds((AppiumBy.CLASS_NAME, "android.widget.TextView"))
        return any(name.lower() in e.text.lower() for e in elements)

    def is_book_in_library(self, book_name):
        try:
            el = self.driver.find_element(
                AppiumBy.XPATH,
                f'//android.widget.TextView[@text="LIBRARY"]/following::android.widget.TextView[contains(@text,"{book_name}")][1]'
            )
            return el.is_displayed()
        except:
            return False

    def wait_for_library(self):
        self.wait_for(lambda d: len(d.find_elements(*self.BOOK)) > 0)
        print("Library loaded")

    def click_first_book(self):
        books = self.driver.find_elements(*self.BOOK)

        if not books:
            raise Exception("No books found")

        print(f"Found {len(books)} books. Clicking first one.")
        books[0].click()