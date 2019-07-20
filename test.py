import ctypes
import sys
from functions import *


if __name__ == '__main__':
    if is_admin():
        while True:
            start_game()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)