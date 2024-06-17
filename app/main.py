from typing import Optional, Tuple, Union
from customtkinter import *
from components.sidebar import SideBar
from pdf_merger.index import BulkPdfMerger
import json


class App(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.title('PDFMergeXpress')
        self.geometry('750x310')
        self.minsize(750, 300)

        with open("app/config.json") as config:
            config = json.load(config)
            appearance_mode = config["appearanceMode"]

        set_appearance_mode(appearance_mode)
        set_default_color_theme('app/assets/themes/metal.json')

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.bulk_merger = BulkPdfMerger(master=self)

        self.sidebar = SideBar(master=self, page1=self.bulk_merger)
        self.sidebar.grid(row=0, column=0, sticky='nsw')


if __name__ == '__main__':
    app = App()
    app.mainloop()
