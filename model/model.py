
from PySide6.QtWidgets import QWidget,QPushButton
from view.view import View


class Model:
    def __init__(self) -> None:
        self.all_menu_buttons = []
        
        
    
    def get_all_menu_buttons(self,obj):
        for button in obj.findChildren(QPushButton):
            self.all_menu_buttons.append(button)
        
            
    
         
    
    
        