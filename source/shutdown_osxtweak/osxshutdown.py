from ui.shutdown_dialog import OSXShutdownDialog

import sys
from PyQt5 import QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = OSXShutdownDialog()
    window.show()

    app.exec_()


if __name__ == "__main__":
    main()
