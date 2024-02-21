from typing import Optional, Tuple, Union
from customtkinter import *
from .appearance_mode_toggler import AppearanceModeToggler


class SideBar(CTkFrame):
    WIDTH = 50

    def __init__(self, *args,
                 page1, page2=None, page3=None,
                 corner_radius: int = 0,
                 **kwargs):
        super().__init__(*args, corner_radius=corner_radius, **kwargs)

        self.page1 = page1
        self.page2 = page2
        self.page3 = page3

        self.sidebar_label = CTkLabel(
            self, text='PDFMergeXpress', font=CTkFont(size=15, weight='bold'))
        self.sidebar_label.grid(row=0, column=0,  padx=20, pady=20)

        self.docx_convert_btn = CTkButton(
            self, text='DOCX to PDF',  height=40, border_spacing=10, corner_radius=corner_radius, fg_color='transparent', text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'), anchor='center', command=lambda: self.select_frame_by_name('single_docx'))
        self.docx_convert_btn.grid(
            row=1, column=0, sticky='ew')

        self.bulk_docx_convert_btn = CTkButton(
            self, text='Bulk DOCX to PDF', height=40, border_spacing=10, corner_radius=corner_radius, fg_color='transparent', text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'), anchor='center', command=lambda: self.select_frame_by_name('bulk_docx'))
        self.bulk_docx_convert_btn.grid(
            row=2, column=0,  sticky='ew')

        self.bulk_merge_btn = CTkButton(
            self, text='Bulk PDF Merger', height=40, border_spacing=10, corner_radius=corner_radius, fg_color='transparent', text_color=('gray10', 'gray90'), hover_color=('gray70', 'gray30'), anchor='center', command=lambda: self.select_frame_by_name('bulk_pdf'))
        self.bulk_merge_btn.grid(
            row=3, column=0, sticky='ew')

        self.appearance_mode_toggler = AppearanceModeToggler(master=self)
        self.appearance_mode_toggler.grid(
            row=4, column=0, padx=10, pady=20, sticky='s')

        # select default frame
        self.select_frame_by_name('bulk_pdf')

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.docx_convert_btn.configure(
            fg_color=('gray65', 'gray40') if name == 'single_docx' else 'transparent')
        self.bulk_docx_convert_btn.configure(
            fg_color=('gray65', 'gray40') if name == 'bulk_docx' else 'transparent')
        self.bulk_merge_btn.configure(
            fg_color=('gray65', 'gray40') if name == 'bulk_pdf' else 'transparent')

        # show selected frame
        if name == 'single_docx':
            self.page1.grid(row=0, column=1, sticky='nsew')
        else:
            self.page1.grid_forget()
        if name == 'bulk_docx':
            self.page2.grid(row=0, column=1, sticky='nsew')
        else:
            self.page2.grid_forget()
        if name == 'bulk_pdf':
            self.page3.grid(row=0, column=1, sticky='nsew')
        else:
            self.page3.grid_forget()


if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)

            self.grid_columnconfigure(0, weight=1)

            self.sidebar = SideBar(self)
            self.sidebar.grid(row=0, column=0, sticky='w')

    app = Tester()

    app.mainloop()
