from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import ui_main
from functions import is_admin
from ctypes import windll


if __name__ == '__main__':
    if is_admin():
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = ui_main.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec())
    else:
        windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
