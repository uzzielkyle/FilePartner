# A combination of a progress bar, button, and my very own searchbar component.
from typing import Optional, Tuple, Union
from customtkinter import *
from components.searchbar import Searchbar
from components.merger import Merger
from utils.pdf_logics import *
import glob


class HeadComponent(CTkFrame):
    WIDTH: int = 500
    HEIGHT: int = 50
    
    def __init__(self, *args, 
                 bg_color: str | Tuple[str, str] = 'transparent', 
                 fg_color: str | Tuple[str, str] = 'whitesmoke', 
                 corner_radius: int = 0,
                 **kwargs):
        super().__init__(*args, bg_color=bg_color, fg_color=fg_color, corner_radius=corner_radius, **kwargs)
                
        self.grid_columnconfigure(0, weight=1)
        
        self.searchbar = Searchbar(master=self)
        self.searchbar.grid(row=0, column=0, padx=10, pady=(5, 0))
    
        self.merger = Merger(master=self, get_path_func=self.searchbar.get, clear_search_func=self.searchbar.clear)
        self.merger.grid(row=1, column=0, padx=10, pady=(0, 5))
            
        
class Tester(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
    
        self.head = HeadComponent(self)
        self.head.grid(row=0, column=0)
        
        
def main():
    app = Tester()
    app.mainloop()
    

if __name__ == '__main__':
    main()
    