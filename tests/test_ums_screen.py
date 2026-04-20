import pytest
import time
from utils.screen_detector import ScreenDetector
from utils.device_actions import reboot_device
from utils.device_screen import unlock_screen
from utils.driver_lifecycle import restart_driver
from utils.driver_setup import get_driver

from pages.ums_page import UmsPage

# This test is goog for now only device reboot, UMS can be on any screen
@pytest.mark.test_id("TC005")
@pytest.mark.reboot(reason="USB state required after boot")
def test_ums(driver):

    time.sleep(30)

    # CRITICAL: restart Appium session after reboot
   # driver = get_driver()

    ums = UmsPage(driver)
   # unlock_screen(driver)
    #Close USB Mode Dialog
    time.sleep(15)
    ums.close_storage()

  #  time.sleep(2)
    # validation (update based on UI)
    detector = ScreenDetector(driver)
    screen = detector.get_current_screen()

    print(f"Leo Detected screen: {screen}")

    assert "EpdHome" in screen
