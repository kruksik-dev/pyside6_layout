
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QVariantAnimation,QEvent,QAbstractAnimation,QSize
from PySide6.QtGui import QColor,QIcon,QEnterEvent
from ..rc_icons import *


class HoverButton(QPushButton):
    def __init__(self, parent=None, color1="#48dbfb", color2="#2e86de"):
        super().__init__(parent)
        
        #colors 
        self.color1 = QColor(color1)
        self.color2 = QColor(color2)
        
        #basic stylesheet
        self.qss = """
            font: 75 10pt;
            font-weight: bold;
            color: #fff;
            border-style: solid;
            border-radius:5px;
            padding:10px;
            """

        #Animation
        self._animation = QVariantAnimation(
            self,
            startValue=0.0001,
            endValue=0.99999,
            duration=250
        )
        
        
        
        #Run _animate when value of animation has been changed
        self._animation.valueChanged.connect(self._animate)
        
        #Set default qss
        self.setStyleSheet(self.qss)

        #Set default grad as background value = 0
        self._animate(0)
        
    def _animate(self, value):
        grad = "background-color: qlineargradient(spread:pad, x1:0, y0:1, x2:1, y2:1, stop:0 {color2}, stop:{value} {color1}, stop: 1 {color2});\n".format(
            color1=self.color1.name(), color2=self.color2.name(), value=value
        )
        self.qss += grad 
        self.setStyleSheet(self.qss)
        
        
    def enterEvent(self, event:QEnterEvent) -> None:
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        return super().enterEvent(event)

    def leaveEvent(self, event:QEvent) -> None:
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        return super().leaveEvent(event)

        

