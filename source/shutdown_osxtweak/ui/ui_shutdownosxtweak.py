# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './assets/shutdownosxtweak.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_shutdownosxtweak(object):
    def setupUi(self, shutdownosxtweak):
        shutdownosxtweak.setObjectName("shutdownosxtweak")
        shutdownosxtweak.resize(600, 158)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(shutdownosxtweak.sizePolicy().hasHeightForWidth())
        shutdownosxtweak.setSizePolicy(sizePolicy)
        shutdownosxtweak.setMinimumSize(QtCore.QSize(600, 158))
        shutdownosxtweak.setMaximumSize(QtCore.QSize(600, 158))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./assets/powerbutton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        shutdownosxtweak.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(shutdownosxtweak)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.power_icon = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.power_icon.sizePolicy().hasHeightForWidth())
        self.power_icon.setSizePolicy(sizePolicy)
        self.power_icon.setMinimumSize(QtCore.QSize(90, 90))
        self.power_icon.setMaximumSize(QtCore.QSize(90, 90))
        self.power_icon.setText("")
        self.power_icon.setPixmap(QtGui.QPixmap("./assets/powerbutton.png"))
        self.power_icon.setScaledContents(True)
        self.power_icon.setObjectName("power_icon")
        self.horizontalLayout_2.addWidget(self.power_icon)
        self.user_description_area = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.user_description_area.setFont(font)
        self.user_description_area.setWordWrap(True)
        self.user_description_area.setObjectName("user_description_area")
        self.horizontalLayout_2.addWidget(self.user_description_area)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnRestart = QtWidgets.QPushButton(self.centralwidget)
        self.btnRestart.setObjectName("btnRestart")
        self.horizontalLayout.addWidget(self.btnRestart)
        self.btnSleep = QtWidgets.QPushButton(self.centralwidget)
        self.btnSleep.setObjectName("btnSleep")
        self.horizontalLayout.addWidget(self.btnSleep)
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.btnShutdown = QtWidgets.QPushButton(self.centralwidget)
        self.btnShutdown.setAutoDefault(True)
        self.btnShutdown.setDefault(True)
        self.btnShutdown.setObjectName("btnShutdown")
        self.horizontalLayout.addWidget(self.btnShutdown)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        shutdownosxtweak.setCentralWidget(self.centralwidget)

        self.retranslateUi(shutdownosxtweak)
        self.btnCancel.released.connect(shutdownosxtweak.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(shutdownosxtweak)

    def retranslateUi(self, shutdownosxtweak):
        _translate = QtCore.QCoreApplication.translate
        shutdownosxtweak.setWindowTitle(_translate("shutdownosxtweak", "macOS Tweaks | Shutdown menu"))
        self.user_description_area.setText(
            _translate("shutdownosxtweak", "Are you sure you want to shut down your computer now?"))
        self.btnRestart.setText(_translate("shutdownosxtweak", "Restart"))
        self.btnSleep.setText(_translate("shutdownosxtweak", "Sleep"))
        self.btnCancel.setText(_translate("shutdownosxtweak", "Cancel"))
        self.btnShutdown.setText(_translate("shutdownosxtweak", "Shut Down"))


