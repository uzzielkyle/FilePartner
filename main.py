from typing import Optional, Tuple, Union
from customtkinter import *
from components.head import HeadComponent 
from utils.pdf_logics import *

        
class App(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
    
        self.head = HeadComponent(self)
        self.head.grid(row=0, column=0)
        
        
def main():
    app = App()
    app.mainloop()
    

if __name__ == '__main__':
    main()
    