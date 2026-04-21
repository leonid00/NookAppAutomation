import pytest

from pages.library_page import LibraryPage


@pytest.mark.test_id("TC007")
#@pytest.mark.home
def test_library_book_search_book():

    library = LibraryPage()

    library.open_search()
    library.search_book("Star Forged (Ascension Gate)")

    assert library.is_book_present("Star Forged (Ascension Gate)")