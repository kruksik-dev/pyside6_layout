# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenLuCRpR.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 596)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#main_frame{\n"
"background-color: #576574;\n"
"border-radius: 50px;\n"
"}\n"
"\n"
"#label {\n"
"color: #ff9ff3;\n"
"font: 36pt \"Segoe UI\";\n"
"}\n"
"\n"
"#desc{\n"
"color: #48dbfb;\n"
"font: 18pt \"Segoe UI\";\n"
"}\n"
"\n"
"QProgressBar{\n"
"background-color:#748699;\n"
"color:#fff;\n"
"border-style:none;\n"
"border-radius:10px;\n"
"text-align:center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.551, x2:1, y2:0.539773, stop:0.346591 rgba(226, 178, 229, 255), stop:0.897727 rgba(194, 137, 242, 255));\n"
"}\n"
"\n"
"#loading{\n"
"color:#fff;\n"
"font: 12pt;\n"
"}\n"
"\n"
"#credits{\n"
"color: #48dbfb;\n"
"font: 700 8pt;\n"
"}")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(90, 90, 651, 383))
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.main_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 50, 421, 61))
        font = QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.desc = QLabel(self.main_frame)
        self.desc.setObjectName(u"desc")
        self.desc.setGeometry(QRect(110, 120, 421, 41))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        self.desc.setFont(font1)
        self.desc.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.main_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 240, 591, 23))
        self.progressBar.setValue(24)
        self.loading = QLabel(self.main_frame)
        self.loading.setObjectName(u"loading")
        self.loading.setGeometry(QRect(150, 270, 341, 41))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.loading.setFont(font2)
        self.loading.setAlignment(Qt.AlignCenter)
        self.credits = QLabel(self.main_frame)
        self.credits.setObjectName(u"credits")
        self.credits.setGeometry(QRect(470, 350, 151, 20))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setItalic(False)
        self.credits.setFont(font3)
        self.credits.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<strong>Kruksik </strong> App Layout", None))
        self.desc.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Basic layout for future procjects</p><p><br/></p></body></html>", None))
        self.loading.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>loading ...</p></body></html>", None))
        self.credits.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>created by: kruksik v1.0.0</p></body></html>", None))
    # retranslateUi

