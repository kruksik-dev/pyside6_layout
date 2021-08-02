
from controller import *
from model import *
from view import *
from PySide6.QtWidgets import QApplication
import sys


class App(QApplication):
    def __init__(self,argv) -> None:
        super(App,self).__init__(argv)
        self.model = Model()
        self.view = View(self.model)
        self.controller = Controller(view=self.view,model=self.model)
        
    
        
if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())