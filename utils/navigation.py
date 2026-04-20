import time
import subprocess


def go_to_home(driver, timeout=15):
    print("Navigating to EpdHomeActivity from any screen...")

    for i in range(timeout):
        try:
            activity = driver.current_activity
            print(f"Attempt {i+1}: {activity}")

            # Target reached
            if "EpdHomeActivity" in activity:
                print(" Reached Home screen")
                return True

            # 🔙 Try BACK via Appium
            try:
                driver.press_keycode(4)
                print("BACK (Appium)")
            except:
                #Fallback to ADB if Appium is unstable
                subprocess.run(["adb", "shell", "input", "keyevent", "4"])
                print("🔙 BACK (ADB fallback)")

        except Exception as e:
            print(f"Driver issue: {e}")

            # fallback when driver is unstable
            subprocess.run(["adb", "shell", "input", "keyevent", "4"])
            print("🔙 BACK (ADB recovery)")

        time.sleep(1)

    # Last fallback → HOME button
    print("BACK didn't work, sending HOME key")

    try:
        driver.press_keycode(3)  # KEYCODE_HOME
    except:
        subprocess.run(["adb", "shell", "input", "keyevent", "3"])

    time.sleep(2)

    # Optional: reopen your app here if needed

    raise Exception("Failed to reach Home screen")