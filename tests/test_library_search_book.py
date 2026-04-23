import pytest
from pages.library_page import LibraryPage

@pytest.mark.home
@pytest.mark.test_id("TC007")
def test_library_search_book(pages):

    #library = LibraryPage(driver)

    # example actions
    pages.home.open_library()
    pages.library.search_book("Star Forged")
   # assert pages.library.is_book_present("Star Forged")
   # assert pages.library.is_book_in_library("Star Forged")
    assert pages.library.is_book_present("Star Forged (Ascension Gate)")
