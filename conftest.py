import pytest
from utils.driver_setup import get_driver
from utils.excel_reader import get_runnable_test_ids
from utils.device_actions import reboot_device
import time, os
from utils.navigation import go_to_home
from appium.options.android import UiAutomator2Options


# ======================================================
# EXCEL TEST FILTER
# ======================================================
def pytest_collection_modifyitems(config, items):
    runnable_ids = get_runnable_test_ids()

    print(f"Runnable from Excel: {runnable_ids}")

    for item in items:
        marker = item.get_closest_marker("test_id")

        # No test_id → skip
        if not marker:
            item.add_marker(pytest.mark.skip(reason="No test_id (Excel control)"))
            continue

        test_id = marker.args[0]

        # Not in Excel RUN=YES → skip
        if test_id not in runnable_ids:
            item.add_marker(
                pytest.mark.skip(reason=f"{test_id} skipped via Excel")
            )


@pytest.fixture(scope="function")
def driver(request):

    test_id_marker = request.node.get_closest_marker("test_id")
    reboot_marker = request.node.get_closest_marker("reboot")
    home_marker = request.node.get_closest_marker("home")

    test_id = test_id_marker.args[0] if test_id_marker else None

    # ======================================================
    # REBOOT LOGIC
    # ======================================================
    if reboot_marker or test_id == "TC005":
        print("Reboot triggered for test")
        reboot_device()

        # CRITICAL FIX: wait AFTER reboot
       # wait_for_device_ready()
        time.sleep(35)  # extra buffer for UiAutomator2 stability

    # extra safety before session start
    time.sleep(3)

    driver = get_driver()


    # ======================================================
    # CRITICAL ADDITION: ALWAYS START FROM HOME STATE
    # ======================================================
    if home_marker:
        print("Moving device to Home screen before test...")
        try:
            go_to_home(driver)
        except Exception as e:
            print(f"Failed to go home: {e}")

    yield driver

    try:
        driver.quit()
    except Exception as e:
        print(f"driver quit ignored: {e}")