import sys

from PyQt5 import QtWidgets

from ui import shutdown_dialog


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = shutdown_dialog.OSXShutdownDialog()
    window.show()

    app.exec_()


if __name__ == "__main__":
    main()
