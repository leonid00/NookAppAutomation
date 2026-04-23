import pytest
from pages.library_filters import LibraryFilters

@pytest.mark.test_id("TC009")
#@pytest.mark.home
def test_library_filters(driver):

    library_filters = LibraryFilters(driver)
    library_filters.click_books()




