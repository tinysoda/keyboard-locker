import platform
from .platform.linux import linux_lock_keyboard ,linux_unlock_keyboard 
from .platform.windows import windows_lock_keyboard, windows_unlock_keyboard

def lock_keyboard():
    if platform.system() == "Linux":
        linux_lock_keyboard()
    elif platform.system() == "Windows":
        windows_lock_keyboard()
    else:
        print("Unsupported platform")

def unlock_keyboard():
    if platform.system() == "Linux":
        linux_unlock_keyboard()
    elif platform.system() == "Windows":
        windows_unlock_keyboard()
    else:
        print("Unsupported platform")

def toggle_keyboard():
    global is_locked
    if is_locked:
        unlock_keyboard()
    else:
        lock_keyboard()
    is_locked = not is_locked