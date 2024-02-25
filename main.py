from typing import Optional, Tuple, Union
from customtkinter import *
from apps.components.sidebar import SideBar
from apps.pdf_merger import BulkPdfMerger
from apps.single_docx_converter import SingleDocxConverter
from apps.bulk_docx_converter import BulkDocxConverter


class App(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.title('PDFMergeXpress')
        self.geometry('750x310')
        self.minsize(750, 300)

        set_appearance_mode('Light')
        set_default_color_theme('assets/themes/metal.json')

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.single_docx_converter = SingleDocxConverter(master=self)
        self.bulk_docx_converter = BulkDocxConverter(master=self)
        self.bulk_merger = BulkPdfMerger(master=self)

        self.sidebar = SideBar(master=self, page1=self.single_docx_converter,
                               page2=self.bulk_docx_converter, page3=self.bulk_merger)
        self.sidebar.grid(row=0, column=0, sticky='nsw')


if __name__ == '__main__':
    app = App()
    app.mainloop()
