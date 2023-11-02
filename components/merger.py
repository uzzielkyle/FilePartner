# Looks like this component would not work hehe
from typing import Optional, Tuple, Union
from customtkinter import *


class Merger(CTkFrame):
    def __init__(self, *args, 
                 width: int = 200, 
                 height: int = 50, 
                 bg_color: str | Tuple[str, str] = 'transparent', 
                 fg_color: str | Tuple[str, str] = 'transparent', 
                 corner_radius: int = 0,
                 **kwargs):
        super().__init__(*args, width=width, height=height, bg_color=bg_color, fg_color=fg_color, corner_radius=corner_radius, **kwargs)
        
        self.folder_path = None
        
        self.grid_columnconfigure((0, 1), weight=1)
            
        
        
    def set_folder_path(self, folder_path) -> str:
        self.folder_path = folder_path
    
    def start_merging(self):
        
        self.progress_bar.start()
        self.merge_btn.configure(state='disabled')
        
    def done_merging(self):
        self.progress_bar.stop()
        self.merge_btn.configure(state='normal')
        

class Tester(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
        
        self.Merger = Merger(master=self, width=750)
        self.Merger.grid(row=0, column=0, padx=10, pady=10)
        
        
def main():
    app = Tester()
    
    app.mainloop()
    

if __name__ == '__main__':
    main()
    