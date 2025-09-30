import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon

from keyboard_locker import controller


def run_tray():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # Prevent app from closing

    # Load tray icon
    icon_path = Path(__file__).parent / "icons" / "tray_icon.png"
    tray_icon = QSystemTrayIcon(QIcon(str(icon_path)), parent=app)
    tray_icon.setToolTip("Keyboard Locker")

    # Create menu
    menu = QMenu()

    lock_action = QAction("Lock Keyboard")
    lock_action.triggered.connect(controller.lock_keyboard)
    menu.addAction(lock_action)

    unlock_action = QAction("Unlock Keyboard")
    unlock_action.triggered.connect(controller.unlock_keyboard)
    menu.addAction(unlock_action)

    exit_action = QAction("Exit")
    exit_action.triggered.connect(app.quit)
    menu.addAction(exit_action)

    # Attach menu
    tray_icon.setContextMenu(menu)
    tray_icon.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    run_tray()
