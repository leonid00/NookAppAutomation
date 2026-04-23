from pages.library_page import LibraryPage
from pages.home_page import HomePage

class PageManager:

    def __init__(self, driver):
        self.driver = driver

        # lazy-loaded pages
        self._library = None
        self._reader = None
        self.home = HomePage(driver)

    @property
    def library(self):
        if self._library is None:
            from pages.library_page import LibraryPage
            self._library = LibraryPage(self.driver)
        return self._library

    @property
    def reader(self):
        if self._reader is None:
            from pages.reader_page import ReaderPage
            self._reader = ReaderPage(self.driver)
        return self._reader
