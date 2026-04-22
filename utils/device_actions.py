import subprocess
import time
from utils.device_screen import unlock_screen

def adb_shell(cmd):
    result = subprocess.run(
        ['adb', 'shell'] + cmd,
        capture_output=True, text=True
    )
    return result.stdout.strip()


def wait_for_device_ready():
    print("⏳ Waiting for device...")

    subprocess.run(["adb", "wait-for-device"])

    while adb_shell(["getprop", "sys.boot_completed"]) != "1":
        time.sleep(3)

    print("✅ Boot completed")

    while adb_shell(["getprop", "init.svc.bootanim"]) != "stopped":
        time.sleep(3)

    print("✅ Boot animation stopped")

    # IMPORTANT: extra stabilization time
    time.sleep(10)

    print("✅ Device ready")


def unlock_device():
    print("🔓 Ensuring device is unlocked...")

    # Wake up screen
    subprocess.run(['adb', 'shell', 'input', 'keyevent', '26'])  # POWER
    time.sleep(1)

    # Swipe up (adjust for your device)
    subprocess.run(['adb', 'shell', 'input', 'swipe', '300', '1000', '300', '300'])
    time.sleep(2)


def wait_for_launcher():
    print("⏳ Waiting for launcher/home screen...")

    while True:
        activity = adb_shell(['dumpsys', 'window', 'windows'])
        if "mCurrentFocus" in activity:
            print("✅ UI responding")
            break
        print("⏳ UI not ready...")
        time.sleep(3)


def ensure_adb_stable():
    print("🔍 Checking ADB stability...")

    for _ in range(5):
        result = subprocess.run(
            ['adb', 'shell', 'echo', 'ping'],
            capture_output=True, text=True
        )
        if result.stdout.strip() == 'ping':
            print("✅ ADB stable")
            return
        time.sleep(2)

    raise Exception("❌ ADB not stable after reboot")


def reboot_device():
    #print("\n🔄 Rebooting device...")
    subprocess.run(['adb', 'reboot'])
    time.sleep(10)
   # wait_for_device_ready()

def press_back():
    subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_BACK'])
    time.sleep(1)
    print("Back key pressed")