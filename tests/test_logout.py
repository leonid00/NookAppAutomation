import pytest

@pytest.mark.test_id("TC003")
@pytest.mark.home
def test_open_book(driver):
    print("Performing logout from NOOK device")
    # Prod EPD devices will close adb connection after deregister