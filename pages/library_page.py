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
        self.find(self.SEARCH_INPUT).send_keys(name)

    def is_book_present(self, name):
        elements = self.finds((AppiumBy.CLASS_NAME, "android.widget.TextView"))
        return any(name.lower() in e.text.lower() for e in elements)

    def wait_for_library(self):
        self.wait_for(lambda d: len(d.find_elements(*self.BOOK)) > 0)
        print("Library loaded")

    def click_first_book(self):
        books = self.driver.find_elements(*self.BOOK)

        if not books:
            raise Exception("No books found")

        print(f"Found {len(books)} books. Clicking first one.")
        books[0].click()