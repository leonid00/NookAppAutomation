import pytest

from utils.screen_detector import ScreenDetector

@pytest.mark.test_id("TC008")
def test_detect_current_screen(driver):
    detector = ScreenDetector(driver)

    screen = detector.get_current_screen()

    print(f"Detected screen: {screen}")

    assert screen in ["WelcomeIntro","Library","Search", "Login", "Reader", "Search", "Shop",
                      "Audiobooks", "Account", "CreateAccount", "SignOutAccount", "EpdHome",
                      "WelcomeToTheNewLibrary", "Tutorial", "EpdProductDetails", "trends", "Wishlist",
                      "FavoriteCategories", "ManageProfiles", "AccountSettings", "PaymentSettings",
                      "AppSet tings", "WifiPicker", "GlowlightSettings", "UsbModeScreen", "Unknown"]