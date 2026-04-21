from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ReaderPage(BasePage):

    SPINNER = (AppiumBy.ID, "bn.ereader:id/sliding_spinner_progress")
    READER = (AppiumBy.ID, "bn.ereader:id/reader_container")
    READER_BOOK_TITLE = (AppiumBy.ID, "bn.ereader:id/reader_book_title")
    READER_SPEED = (By.ID, "bn.ereader:id/reading_speed_in_chapter_info")
    READER_PROGRESS = (AppiumBy.ID, "bn.ereader:id/reader_page_progress_info")
    FIRST_BOOK = (AppiumBy.ANDROID_UIAUTOMATOR,
                  'new UiSelector().resourceId("bn.ereader:id/cover_border").instance(0)') # first book in library

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #open first book i the list from Library
    def open_first_book(self):
        self.wait.until(lambda d: d.find_element(*self.FIRST_BOOK)).click()


    def wait_for_book_loaded(self):
        self.wait_invisible(self.SPINNER)
        self.wait_visible(self.READER_BOOK_TITLE)