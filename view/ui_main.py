# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainDAAcoS.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from .rc_icons import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1064, 730)
        MainWindow.setMinimumSize(QSize(1030, 716))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* #############################################\n"
"MAIN QSS FILE\n"
"EACH STYLE SHOULD BE CHANGE | ADD HERE NOT IN SEPARATED ELEMENTS \n"
"ONLY INDIVIDUALS STAFF SHOULD BE ADDED ALONE (ICONS,IMG) BUT NOT CORE\n"
"\n"
"############################################### */\n"
"\n"
"/* ######### WIDGET ############ */\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"/* ######### TOOLTIP ############ */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color:  #CC576574;\n"
"	border: 1px solid #8395a7;\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid #c8d6e5;\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"\n"
"/* ######### BACKGROUND ############ */\n"
"#background {\n"
"	background-color:  #2f3542;\n"
"	border: 1px solid #202c3b;\n"
"		\n"
"}\n"
"\n"
"/* ######### LEFT MENU ############ */\n"
"#LeftMenuFrame {\n"
"	background-color:"
                        "  #57606f;\n"
"}\n"
"/* ######### LEFT MENU HIDDEN ############ */\n"
"#ExtraLeftMenuFrame {\n"
"	background-color:  #227093;\n"
"    border-top: 4px solid #202c3b;\n"
"}\n"
"\n"
"/* ######### MAIN BUTTONS FRAME ############ */\n"
"#mainbuttonsframe {\n"
"	border-top: 4px solid #202c3b;\n"
"}\n"
"/* ######### TOGGLE BUTTON ############ */\n"
"#ToggleButton, #SettingsButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"    text-align: left;\n"
"	border-left: 20px solid transparent;\n"
"	padding-left: 44px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#SettingsButton:pressed, #ToggleButton:pressed {	\n"
"	background-color:  #f368e0;\n"
"	color: #000;\n"
"}\n"
"\n"
"/* ######### BUTTONS  MENU LEFT SIDE ############ */\n"
"#buttonsframe .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
""
                        "}\n"
"#buttonsframe .QPushButton:hover{\n"
"	background-color: #2f3542;\n"
"	border-left: 26px solid transparent;\n"
"}\n"
"#buttonsframe .QPushButton:pressed {	\n"
"	background-color:  #48dbfb;\n"
"	color: #000;\n"
"}\n"
"\n"
"/* ######### TOPBAR ############ */\n"
"#topbarframe{\n"
"	background-color:  #57606f;\n"
"}\n"
"\n"
"\n"
"/* ######### APPICON ############ */\n"
"#appicon{\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	border-left: 10px solid transparent;\n"
"}\n"
"\n"
"/* ######### TOP BUTTONS ############ */\n"
"#closebuttonframe .QPushButton{ \n"
"    background-color: transparent ;\n"
"    border: none;  \n"
"    border-radius: 5px; \n"
"}\n"
"#closebuttonframe .QPushButton:hover { \n"
"   border-style: solid; \n"
"   border-radius: 4px; \n"
"}\n"
"\n"
"#closeButton:hover{\n"
"   background-color: #ff6b6b;\n"
"}\n"
"\n"
"#maximizeButton:hover{\n"
"   background-color: #feca57;\n"
"}\n"
"\n"
"#minimizeButton:"
                        "hover{\n"
"   background-color: #1dd1a1;\n"
"}\n"
"\n"
"#closebuttonframe .QPushButton:pressed{ \n"
"   border-style: solid; \n"
"   border-radius: 4px; \n"
"}\n"
"\n"
"#closeButton:pressed{\n"
"   background-color: #ee5253;\n"
"}\n"
"\n"
"#maximizeButton:pressed{\n"
"   background-color: #ff9f43;\n"
"}\n"
"\n"
"#minimizeButton:pressed{\n"
"   background-color: #159472;\n"
"}\n"
"\n"
"\n"
"\n"
"/* ######### FOOTER ############ */\n"
"#footer { \n"
"    background-color: #3f4759;\n"
"}\n"
"#footer QLabel { \n"
"    font-size: 11px;\n"
"    color: #c8d6e5;\n"
"    padding-left: 12px; \n"
"    padding-right: 10px; \n"
"    padding-bottom: 2px;\n"
"}\n"
"#resizeicon{\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 10px solid transparent;\n"
"	border-top: 8px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"}\n"
"\n"
"/* ######### CENTRALFRAME ############ */\n"
"#centralframe {\n"
"	border-top: 4px solid #202c3b;\n"
""
                        "}\n"
"\n"
"/*########## STACKEDWIDGET PAGES ################### */\n"
"#title_page_content QLabel{\n"
"   font: 700 72pt \"Segoe UI\";\n"
"   color: #54a0ff;\n"
"}\n"
"/*############# EXTRA LEFT MENU #####################*/\n"
"#extralefttext{\n"
"	background:transparent;\n"
"	border:none;\n"
"}\n"
"")
        self.CentralAppMargins = QVBoxLayout(self.centralwidget)
        self.CentralAppMargins.setSpacing(0)
        self.CentralAppMargins.setObjectName(u"CentralAppMargins")
        self.CentralAppMargins.setContentsMargins(10, 10, 10, 10)
        self.background = QFrame(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setToolTipDuration(-1)
        self.background.setFrameShape(QFrame.NoFrame)
        self.background.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.background)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuFrame = QFrame(self.background)
        self.LeftMenuFrame.setObjectName(u"LeftMenuFrame")
        self.LeftMenuFrame.setMinimumSize(QSize(60, 0))
        self.LeftMenuFrame.setMaximumSize(QSize(60, 16777215))
        self.LeftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.LeftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topbuttonframe = QFrame(self.LeftMenuFrame)
        self.topbuttonframe.setObjectName(u"topbuttonframe")
        self.topbuttonframe.setMaximumSize(QSize(16777215, 50))
        self.topbuttonframe.setFrameShape(QFrame.NoFrame)
        self.topbuttonframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.topbuttonframe)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ToggleButton = QPushButton(self.topbuttonframe)
        self.ToggleButton.setObjectName(u"ToggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToggleButton.sizePolicy().hasHeightForWidth())
        self.ToggleButton.setSizePolicy(sizePolicy)
        self.ToggleButton.setMinimumSize(QSize(0, 0))
        self.ToggleButton.setMaximumSize(QSize(16777215, 50))
        self.ToggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ToggleButton.setStyleSheet(u"background-image: url(:/icons/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.ToggleButton)


        self.verticalLayout_2.addWidget(self.topbuttonframe)

        self.mainbuttonsframe = QFrame(self.LeftMenuFrame)
        self.mainbuttonsframe.setObjectName(u"mainbuttonsframe")
        self.mainbuttonsframe.setFrameShape(QFrame.NoFrame)
        self.mainbuttonsframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.mainbuttonsframe)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.buttonsframe = QFrame(self.mainbuttonsframe)
        self.buttonsframe.setObjectName(u"buttonsframe")
        self.buttonsframe.setFrameShape(QFrame.NoFrame)
        self.buttonsframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.buttonsframe)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.buttonsframe)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/icons/cil-house.png);\n"
"")

        self.verticalLayout_6.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.buttonsframe)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 60))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/icons/cil-cloud-upload.png);")

        self.verticalLayout_6.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.buttonsframe)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 60))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/icons/cil-pencil.png);")

        self.verticalLayout_6.addWidget(self.btn_new)

        self.btn_save = QPushButton(self.buttonsframe)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 60))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.buttonsframe)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 60))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_exit)


        self.verticalLayout_3.addWidget(self.buttonsframe)

        self.sep_frame = QFrame(self.mainbuttonsframe)
        self.sep_frame.setObjectName(u"sep_frame")
        self.sep_frame.setFrameShape(QFrame.StyledPanel)
        self.sep_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.sep_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.sep_frame)

        self.extramenubuttonframe = QFrame(self.mainbuttonsframe)
        self.extramenubuttonframe.setObjectName(u"extramenubuttonframe")
        self.extramenubuttonframe.setMaximumSize(QSize(16777215, 50))
        self.extramenubuttonframe.setCursor(QCursor(Qt.PointingHandCursor))
        self.extramenubuttonframe.setFrameShape(QFrame.NoFrame)
        self.extramenubuttonframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extramenubuttonframe)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.SettingsButton = QPushButton(self.extramenubuttonframe)
        self.SettingsButton.setObjectName(u"SettingsButton")
        sizePolicy.setHeightForWidth(self.SettingsButton.sizePolicy().hasHeightForWidth())
        self.SettingsButton.setSizePolicy(sizePolicy)
        self.SettingsButton.setMinimumSize(QSize(0, 0))
        self.SettingsButton.setMaximumSize(QSize(16777215, 50))
        self.SettingsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.SettingsButton.setStyleSheet(u"background-image: url(:/icons/icons/icon_settings.png);")

        self.verticalLayout_5.addWidget(self.SettingsButton)


        self.verticalLayout_3.addWidget(self.extramenubuttonframe)


        self.verticalLayout_2.addWidget(self.mainbuttonsframe)


        self.horizontalLayout.addWidget(self.LeftMenuFrame)

        self.MainContentFrame = QFrame(self.background)
        self.MainContentFrame.setObjectName(u"MainContentFrame")
        self.MainContentFrame.setFrameShape(QFrame.NoFrame)
        self.MainContentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.MainContentFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.topbarframe = QFrame(self.MainContentFrame)
        self.topbarframe.setObjectName(u"topbarframe")
        self.topbarframe.setMinimumSize(QSize(0, 50))
        self.topbarframe.setMaximumSize(QSize(16777215, 50))
        self.topbarframe.setFrameShape(QFrame.NoFrame)
        self.topbarframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.topbarframe)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 10, 0)
        self.titleframe = QFrame(self.topbarframe)
        self.titleframe.setObjectName(u"titleframe")
        self.titleframe.setFrameShape(QFrame.StyledPanel)
        self.titleframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titleframe)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.appicon = QFrame(self.titleframe)
        self.appicon.setObjectName(u"appicon")
        self.appicon.setMaximumSize(QSize(16777215, 45))
        self.appicon.setStyleSheet(u"background-image: url(:/icons/icons/cil-terminal.png);")
        self.appicon.setFrameShape(QFrame.StyledPanel)
        self.appicon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.appicon)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.horizontalLayout_2.addWidget(self.appicon)

        self.label = QLabel(self.titleframe)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(16777215, 45))

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout_4.addWidget(self.titleframe)

        self.closebuttonframe = QFrame(self.topbarframe)
        self.closebuttonframe.setObjectName(u"closebuttonframe")
        self.closebuttonframe.setMinimumSize(QSize(0, 28))
        self.closebuttonframe.setFrameShape(QFrame.NoFrame)
        self.closebuttonframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.closebuttonframe)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.closebuttonframe)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMinimumSize(QSize(28, 28))
        self.minimizeButton.setMaximumSize(QSize(28, 28))
        self.minimizeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon)
        self.minimizeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.minimizeButton)

        self.maximizeButton = QPushButton(self.closebuttonframe)
        self.maximizeButton.setObjectName(u"maximizeButton")
        self.maximizeButton.setMinimumSize(QSize(28, 28))
        self.maximizeButton.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maximizeButton.setFont(font1)
        self.maximizeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximizeButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeButton.setIcon(icon1)
        self.maximizeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.maximizeButton)

        self.closeButton = QPushButton(self.closebuttonframe)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(28, 28))
        self.closeButton.setMaximumSize(QSize(28, 28))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.horizontalLayout_4.addWidget(self.closebuttonframe)


        self.verticalLayout_8.addWidget(self.topbarframe)

        self.bottomcontentframe = QFrame(self.MainContentFrame)
        self.bottomcontentframe.setObjectName(u"bottomcontentframe")
        self.bottomcontentframe.setFrameShape(QFrame.NoFrame)
        self.bottomcontentframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.bottomcontentframe)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ExtraLeftMenuFrame = QFrame(self.bottomcontentframe)
        self.ExtraLeftMenuFrame.setObjectName(u"ExtraLeftMenuFrame")
        self.ExtraLeftMenuFrame.setMinimumSize(QSize(0, 0))
        self.ExtraLeftMenuFrame.setMaximumSize(QSize(0, 16777215))
        self.ExtraLeftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.ExtraLeftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.ExtraLeftMenuFrame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.extralefttext = QTextEdit(self.ExtraLeftMenuFrame)
        self.extralefttext.setObjectName(u"extralefttext")

        self.verticalLayout_18.addWidget(self.extralefttext)


        self.horizontalLayout_6.addWidget(self.ExtraLeftMenuFrame)

        self.centralmainframe = QFrame(self.bottomcontentframe)
        self.centralmainframe.setObjectName(u"centralmainframe")
        self.centralmainframe.setFrameShape(QFrame.NoFrame)
        self.centralmainframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.centralmainframe)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.centralframe = QFrame(self.centralmainframe)
        self.centralframe.setObjectName(u"centralframe")
        self.centralframe.setFrameShape(QFrame.StyledPanel)
        self.centralframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.centralframe)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.stackedWidget = QStackedWidget(self.centralframe)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: transparent;")
        self.title_page = QWidget()
        self.title_page.setObjectName(u"title_page")
        self.verticalLayout = QVBoxLayout(self.title_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_page_content = QFrame(self.title_page)
        self.title_page_content.setObjectName(u"title_page_content")
        self.title_page_content.setFrameShape(QFrame.StyledPanel)
        self.title_page_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.title_page_content)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_3 = QLabel(self.title_page_content)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.title_page_content)

        self.stackedWidget.addWidget(self.title_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_11 = QVBoxLayout(self.home_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.main_home_page = QFrame(self.home_page)
        self.main_home_page.setObjectName(u"main_home_page")
        self.main_home_page.setFrameShape(QFrame.StyledPanel)
        self.main_home_page.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.main_home_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.textEdit = QTextEdit(self.main_home_page)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_14.addWidget(self.textEdit)


        self.verticalLayout_11.addWidget(self.main_home_page)

        self.stackedWidget.addWidget(self.home_page)
        self.next_page = QWidget()
        self.next_page.setObjectName(u"next_page")
        self.verticalLayout_15 = QVBoxLayout(self.next_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.content_next_page = QFrame(self.next_page)
        self.content_next_page.setObjectName(u"content_next_page")
        self.content_next_page.setFrameShape(QFrame.StyledPanel)
        self.content_next_page.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.content_next_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_2 = QLabel(self.content_next_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 72pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_2)


        self.verticalLayout_15.addWidget(self.content_next_page)

        self.stackedWidget.addWidget(self.next_page)

        self.verticalLayout_13.addWidget(self.stackedWidget)


        self.verticalLayout_9.addWidget(self.centralframe)

        self.footer = QFrame(self.centralmainframe)
        self.footer.setObjectName(u"footer")
        self.footer.setMaximumSize(QSize(16777215, 22))
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.credits = QLabel(self.footer)
        self.credits.setObjectName(u"credits")
        self.credits.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout_5.addWidget(self.credits)

        self.version = QLabel(self.footer)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.resizeicon = QFrame(self.footer)
        self.resizeicon.setObjectName(u"resizeicon")
        self.resizeicon.setMaximumSize(QSize(20, 16777215))
        self.resizeicon.setStyleSheet(u"background-image: url(:/icons/icons/cil-size-grip.png);")
        self.resizeicon.setFrameShape(QFrame.NoFrame)
        self.resizeicon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.resizeicon)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.resizeicon)


        self.verticalLayout_9.addWidget(self.footer)


        self.horizontalLayout_6.addWidget(self.centralmainframe)


        self.verticalLayout_8.addWidget(self.bottomcontentframe)


        self.horizontalLayout.addWidget(self.MainContentFrame)


        self.CentralAppMargins.addWidget(self.background)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ToggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_save.setText("")
        self.btn_exit.setText("")
        self.SettingsButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Kruksik Layout App - Default layout for future projects", None))
#if QT_CONFIG(tooltip)
        self.minimizeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeButton.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeButton.setText("")
#if QT_CONFIG(tooltip)
        self.closeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeButton.setText("")
        self.extralefttext.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffaaff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffaaff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-lef"
                        "t:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffaaff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffaaff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffaaff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffaaff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffaaff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:"
                        "#ffaaff;\">Additional</span> <span style=\" color:#ffffff;\">setting page </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Can u use for some setting </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">or </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; tex"
                        "t-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">diplay information about GUI</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Next Page", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; color:#2bd6df;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; color:#2bd6df;\"><br /></p>\n"
"<p align=\"center\" style=\""
                        "-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; color:#2bd6df;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; color:#2bd6df;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; color:#2bd6df;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#2bd6df;\">Kruksik Layout</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0"
                        "px;\"><span style=\" color:#ffffff;\">Main page of layout</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: kruksik</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Next Page", None))
        self.credits.setText(QCoreApplication.translate("MainWindow", u"Layout created by kruks ", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

