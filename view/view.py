
from view.ui_main import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QPushButton, QSizeGrip
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PySide6.QtGui import QColor, QIcon
from view.custom_modules import SlidingStackedWidget, Splashscreen


class View(QMainWindow):
    def __init__(self, model) -> None:
        super(View, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = model

        self.setWindowTitle("Kruksik QT Layout")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.grip = QSizeGrip(self.ui.resizeicon)
        self.grip.setStyleSheet('background: transparent')

        self.splashscreen = Splashscreen(self)

    def toggleMenu(self, status):

        if self.sender().objectName() == 'ToggleButton':
            layout = self.ui.LeftMenuFrame
            maxExtend = 160
            standard = 60
        else:
            layout = self.ui.ExtraLeftMenuFrame
            maxExtend = 160
            standard = 0

        if not status:
            width = layout.width()

            if width == standard:
                widthToExtend = maxExtend
            else:
                widthToExtend = standard

            self.animation = QPropertyAnimation(layout, b'minimumWidth')
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthToExtend)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    def enable_shadow_effect(self, widget, blur, xoff, yoff):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(blur)
        shadow.setXOffset(xoff)
        shadow.setYOffset(yoff)
        shadow.setColor(QColor(0, 0, 0, 80))
        widget.setGraphicsEffect(shadow)

    ###### Event func #####

    def maximize_windowsize(self):
        if not self.isMaximized():
            self.showMaximized()
            self.ui.CentralAppMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeButton.setToolTip("Restore")
            self.ui.maximizeButton.setIcon(
                QIcon(u":/icons/icons/icon_restore.png"))
            self.ui.resizeicon.hide()

        else:
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.CentralAppMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeButton.setToolTip("Maximize")
            self.ui.maximizeButton.setIcon(
                QIcon(u":/icons/icons/icon_maximize.png"))
            self.ui.resizeicon.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def replaceWidgetsToCustom(self):
        self.ui.stackedWidget.deleteLater()
        self.ui.stackedWidget = SlidingStackedWidget()
        self.ui.stackedWidget.setObjectName(u"stackedWidget")
        self.ui.verticalLayout_13.addWidget(self.ui.stackedWidget)
        self.ui.stackedWidget.addWidget(self.ui.home_page)
        self.ui.stackedWidget.addWidget(self.ui.next_page)
        self.ui.stackedWidget.addWidget(self.ui.title_page)

        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        
    def change_clicked_button_layout(self,buttonstyle):
        new_layout = buttonstyle + self.model.pressedbuttonstyle
        return new_layout
    
    def rechange_clicked_button_layout(self,buttonstyle):
        relayout = buttonstyle.replace(self.model.pressedbuttonstyle, "")
        return relayout
    
    def select_clicked_style(self, button):
        for b in self.ui.buttonsframe.findChildren(QPushButton):
            if b.objectName() == button.objectName():
                b.setStyleSheet(self.change_clicked_button_layout(b.styleSheet()))
    
    def reset_clicked_style(self, button):
        for b in self.ui.buttonsframe.findChildren(QPushButton):
            if b.objectName() != button.objectName():
                b.setStyleSheet(self.rechange_clicked_button_layout(b.styleSheet()))
    
    
    def changePage(self, button):
        slideto = self.model.check_which_slide(button)
        self.reset_clicked_style(button)
        self.select_clicked_style(button)
        self.ui.stackedWidget.slidetowidget(slideto)
