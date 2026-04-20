import pytest
from pages.reader_page import ReaderPage

@pytest.mark.test_id("TC002")
@pytest.mark.home
def test_open_book(driver):
    reader = ReaderPage(driver)

    print("Opening first book...")
    reader.open_first_book()

    print("Waiting for load...")
    reader.wait_for_book_loaded()

    print("Book opened successfully")