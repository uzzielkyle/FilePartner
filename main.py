from typing import Optional, Tuple, Union
from customtkinter import *
from components import HeadComponent 
from components import TreeView
        
class App(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.title('PDFMergeXpress')
        self.geometry('700x310')
        self.minsize(625, 300)
        set_appearance_mode('Light')
        # set_default_color_theme('assets/themes/metal.json')
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
    
        self.head = HeadComponent(self)
        self.head.grid(row=0, column=1, pady=0, sticky='ew')
        
        self.treeview = TreeView(self)
        self.treeview.grid(row=1, column=1, pady=0, sticky='nsew')
               
        self.head.merger.set_treeview_connection(self.treeview.clear, 
                                                 self.treeview.display_outputs)
        
       
if __name__ == '__main__':
    app = App()
    app.mainloop()