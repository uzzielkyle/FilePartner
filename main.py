from typing import Optional, Tuple, Union
from customtkinter import *
from components.head import HeadComponent 
from components.treeview import TreeView
from utils.pdf_logics import *

        
class App(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.title('PDFMergeXpress')
        self.geometry('700x310')
        self.minsize(650, 300)
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
    
        self.head = HeadComponent(self)
        self.head.grid(row=0, column=1, pady=0, sticky='ew')
        
        self.treeview = TreeView(self)
        self.treeview.grid(row=1, column=1, pady=0, sticky='nsew')
               
        self.head.merger.set_treeview_connection(self.treeview.clear, 
                                                 self.treeview.display_folders, 
                                                 self.treeview.display_pdfs)
        
        
def main():
    app = App()
    app.mainloop()
    

if __name__ == '__main__':
    main()
    