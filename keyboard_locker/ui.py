import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon

from keyboard_locker import controller
locked=False
def onTrayActivated(reason,tray_icon):
    global locked
    if reason==QSystemTrayIcon.Trigger:
        if locked:
            controller.unlock_keyboard()
            tray_icon.showMessage("Keyboard locker","Unlocked",QSystemTrayIcon.Information,2000)
            locked=False
        else:
            controller.lock_keyboard()
            tray_icon.showMessage("Keyboard locker","Locked",QSystemTrayIcon.Information,2000)
            locked=True

def run_tray():
    app=QApplication(sys.argv)
    icon_path=Path(__file__).parent/"icons"/"tray_icon.png"
    tray_icon=QSystemTrayIcon(QIcon(str(icon_path)),parent=app)
    tray_icon.setToolTip("Keyboard Locker")

    menu=QMenu()
    exit_action=QAction("Exit")
    exit_action.triggered.connect(app.quit)
    menu.addAction(exit_action)
    tray_icon.setContextMenu(menu)
    tray_icon.activated.connect(lambda reason: onTrayActivated(reason,tray_icon))

    tray_icon.show()
    sys.exit(app.exec())

if __name__=="__main__":
    run_tray()