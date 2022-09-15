import os

from PyQt5 import QtWidgets

import ui_shutdownosxtweak


class OSXShutdownDialog(QtWidgets.QMainWindow, ui_shutdownosxtweak.Ui_shutdownosxtweak):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #############
        # Connect buttons to system shudown scenaries
        self.btnRestart.released.connect(self.restart_mac)
        self.btnSleep.released.connect(self.sleep_mac)
        self.btnShutdown.released.connect(self.shutdown_mac)

    def restart_mac(self):
        os.system("shutdown -r now")

    def sleep_mac(self):
        os.system("shutdown -s now")

    def shutdown_mac(self):
        os.system("shutdown -h now")
