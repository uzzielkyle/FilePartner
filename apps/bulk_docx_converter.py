from typing import Tuple
from customtkinter import *
from components.converter_head import HeadComponent


class BulkDocxConverter(CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = 'transparent', fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color,
                         border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.head = HeadComponent(self)
        self.head.grid(row=0, column=0, sticky='nsew')


if __name__ == '__main__':
    app = BulkDocxConverter()
    app.mainloop()
