from typing import Optional, Tuple, Union
from customtkinter import *


class Searchbar(CTkFrame):
    WIDTH: int = 600
    HEIGHT: int = 50
    
    def __init__(self, *args, 
                 label: str = 'Search Folder:',
                 placeholder_text: str = 'Folder Path',
                 bg_color: str | Tuple[str, str] = 'transparent', 
                 fg_color: str | Tuple[str, str] = 'transparent', 
                 corner_radius: int = 0,
                 **kwargs):
        super().__init__(*args, bg_color=bg_color, fg_color=fg_color, corner_radius=corner_radius, **kwargs)
              
        self.grid_columnconfigure((0, 2), weight=0)
        self.grid_columnconfigure(1, weight=1)
        
        self.lbl_search = CTkLabel(self, text=label, width=90)
        self.lbl_search.grid(row=0, column=0, padx=0, pady=(10,5))
        
        self.entry = CTkEntry(self, placeholder_text=placeholder_text, width=self.WIDTH - 210)
        self.entry.grid(row=0, column=1, padx=10, pady=(10,5), sticky='ew')
        self.entry.bind('<Return>', self.remove_entry_focus)
        
        self.load_btn = CTkButton(self, text="Load", width=90, command=self.load, corner_radius=corner_radius)
        self.load_btn.grid(row=0, column=2, padx=(10,0) , pady=(10,5))
        
    def remove_entry_focus(self, event):
        self.focus()
        
    def load(self):
        folder_path = filedialog.askdirectory()
        
        if folder_path:
            self.clear()
            self.set(folder_path=folder_path)
                    
    def get(self) -> str:
        return self.entry.get()
    
    def set(self, folder_path: str):
        self.clear()
        self.entry.insert(0, folder_path)
        
    def clear(self):
        self.entry.delete(0, 'end')
        self.entry.configure(placeholder_text='Folder Path')
        
        
class Tester(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
    
        self.head_frame = CTkFrame(self, fg_color='whitesmoke', corner_radius=0)
        self.head_frame.grid(row=0, column=0)
        
        self.searchbar = Searchbar(master=self.head_frame, width=700)
        self.searchbar.grid(row=0, column=0, padx=10, pady=(10, 0))
        
        # self.merger = Merger(master=self.head_frame, width=700)
        # self.merger.grid(row=1, column=0, padx=10, pady=(0, 10))
        
        
def main():
    app = Tester()
    
    app.mainloop()
    

if __name__ == '__main__':
    main()
    