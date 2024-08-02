from typing import Optional, Tuple, Union
from customtkinter import *

class AppearanceModeToggler(CTkFrame):
    def __init__(self, *args, 
                 width: int = 100, 
                 height: int = 100, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] = "transparent", 
                 corner_radius: int = 0,
                 **kwargs):
        super().__init__(*args, width=width, height=height, bg_color=bg_color, fg_color=fg_color, corner_radius=corner_radius, **kwargs)
        
        self.grid_rowconfigure(1, weight=1)
        
        self.modes_list = ['System', 'Dark', 'Light']
        
        self.current_mode_var = StringVar(value='System')
        
        self.widget_label = CTkLabel(self, text='Appearance Mode', anchor='center')
        self.widget_label.grid(row=0, column=0, padx=15, pady=0)
        
        self.dropdown_menu = CTkOptionMenu(self, values=self.modes_list, variable=self.current_mode_var, command=self.set)
        self.dropdown_menu.grid(row=1, column=0, padx=10, pady=(0, 5), sticky='ew')
        
    def set(self, choice) -> None:
        try:
            set_appearance_mode(choice)
            
        except ValueError:
            return
        
    def get(self) -> str:
        print(self.dropdown_menu.get())
    

if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            
            self.appearance_mode_toggler = AppearanceModeToggler(master=self)
            self.appearance_mode_toggler.grid(row=0, column=0, padx=10, pady=10)
        
        
    app = Tester()
    
    app.mainloop()
    