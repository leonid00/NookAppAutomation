import pytest

@pytest.mark.test_id("TC006")
@pytest.mark.home
def test_home(driver):
    activity = driver.current_activity
    assert "EpdHomeActivity" in activity