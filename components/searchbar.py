from typing import Tuple
from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton

class Searchbar(CTkFrame):
    def __init__(self, *args, 
                 label: str = '',
                 width: int = 200, 
                 height: int = 50, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 **kwargs):
        super().__init__(*args, width=width, height=height, bg_color=bg_color, **kwargs)
              
        self.grid_columnconfigure((0, 2), weight=0)
        self.grid_columnconfigure(1, weight=1)
        
        self.lbl_search = CTkLabel(self, text=label)
        self.lbl_search.grid(row=0, column=0, padx=(10, 0), pady=5)
        
        self.entry = CTkEntry(self, placeholder_text='Folder path', width=(width // 2))
        self.entry.grid(row=0, column=1, padx=10, pady=5, stick='ew')
        self.entry.bind('<Return>', self.bind_callback)
        
        self.load_btn = CTkButton(self, text="Load", width=(2*height)-10)
        self.load_btn.grid(row=0, column=2, padx=(0, 10), pady=5)
        
    def bind_callback(self, event):
        self.focus()
        print(self.get())
        
    def get(self) -> str:
        return self.entry.get()
    
    def set(self, folder_path: str):
        self.entry.delete(0, 'end')
        self.entry.insert(0, folder_path)
        
        
class App(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
        
        self.searchbar = Searchbar(master=self, label='Search Folder:', width=500)
        self.searchbar.grid(row=0, column=0, padx=10, pady=10)
        
        
def main():
    app = App()
    
    app.mainloop()
    

if __name__ == '__main__':
    main()
    