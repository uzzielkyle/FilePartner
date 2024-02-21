from typing import Optional, Tuple, Union
from customtkinter import *
from components.sidebar import SideBar

if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)

            self.grid_columnconfigure(0, weight=1)
            self.grid_rowconfigure(0, weight=1)

            self.sidebar = SideBar(self)
            self.sidebar.grid(row=0, column=0, sticky='nsw')

    app = Tester()

    app.mainloop()
