from typing import Tuple
from customtkinter import *
from .components.merger_head import MergerHead
from .components.treeview import TreeView


class BulkPdfMerger(CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = 'transparent', fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color,
                         border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.head = MergerHead(self)
        self.head.grid(row=0, column=1, pady=0, sticky='ew')

        self.treeview = TreeView(self)
        self.treeview.grid(row=1, column=1, pady=0, sticky='nsew')

        self.head.merger.set_treeview_connection(self.treeview.clear,
                                                 self.treeview.display_outputs)


if __name__ == '__main__':
    app = BulkPdfMerger()
    app.mainloop()
