import platform
from .platform.linux import lock_keyboard as linux_lock, unlock_keyboard as linux_unlock
from .platform.windows import lock_keyboard as windows_lock, unlock_keyboard as windows_unlock

def lock_keyboard():
    if platform.system() == "Linux":
        linux_lock()
    elif platform.system() == "Windows":
        windows_lock()
    else:
        print("Unsupported platform")

def unlock_keyboard():
    if platform.system() == "Linux":
        linux_unlock()
    elif platform.system() == "Windows":
        windows_unlock()
    else:
        print("Unsupported platform")

