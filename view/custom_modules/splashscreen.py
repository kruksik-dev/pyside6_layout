from PySide6.QtWidgets import QMainWindow
from .ui_splash_screen import Ui_MainWindow
from PySide6.QtCore import Qt, QTimer

progressbar_counter = 0

class Splashscreen(QMainWindow):
    def __init__(self,main_window) -> None:
        QMainWindow.__init__(self)

        self.sp = Ui_MainWindow()
        self.sp.setupUi(self)
        self.main = main_window
        
        
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.timer = QTimer()
        self.timer.start(60)

        self.show()
    
    def progress(self):
        global progressbar_counter
        self.sp.progressBar.setValue(progressbar_counter)
        
        if progressbar_counter == 5:
            self.sp.loading.setText("Preparation for creating a layout ...")
            
        if progressbar_counter == 50:
            self.sp.loading.setText("Connecting to database ...")
            
        if progressbar_counter == 90:
            self.sp.loading.setText("GUI creating ...")
        
        if progressbar_counter > 100:
            self.timer.stop()
            self.main.show()
            self.close()
        
        progressbar_counter +=1
        
    def moveWindow(self,event):
        if self.isMaximized(): self.maximize_restore()
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
            
    def mousePressEvent(self,event):
        self.dragPos = event.globalPos()
            
        
        

   